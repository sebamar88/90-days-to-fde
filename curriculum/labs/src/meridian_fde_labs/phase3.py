"""Bounded tools and approval-gated workflow used by the Phase 3 lab."""

from __future__ import annotations

import copy
import hashlib
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType
from typing import Callable, TypeVar


class AccessDenied(PermissionError):
    """The trusted actor context does not permit the requested operation."""


class InvalidTransition(ValueError):
    """The requested state transition is not valid for this workflow."""


class TransientDependencyError(RuntimeError):
    """A dependency may recover and the read-only operation may be retried."""


DRAFT_FIELDS = frozenset({"category", "urgency", "summary"})


@dataclass(frozen=True)
class Actor:
    subject: str
    role: str
    region: str


@dataclass(frozen=True)
class Preview:
    request_id: str
    site_code: str
    site_id: str
    region: str
    environment: str
    fields: Mapping[str, str]
    preview_hash: str

    def __post_init__(self) -> None:
        if not isinstance(self.fields, Mapping):
            raise ValueError("preview fields must be a mapping")
        copied = dict(self.fields)
        if any(not isinstance(key, str) or not isinstance(value, str) for key, value in copied.items()):
            raise ValueError("preview fields must contain strings")
        if copied.keys() - DRAFT_FIELDS or any(not value.strip() or len(value) > 280 for value in copied.values()):
            raise ValueError("preview fields are invalid")
        for value in (self.request_id, self.site_code, self.site_id, self.region):
            if not isinstance(value, str) or not value.strip():
                raise ValueError("preview identifiers must be non-empty strings")
        if self.environment != "sandbox" or not re.fullmatch(r"[a-f0-9]{64}", self.preview_hash):
            raise ValueError("preview metadata is invalid")
        object.__setattr__(self, "fields", MappingProxyType(dict(sorted(copied.items()))))


def _preview_digest(
    request_id: str,
    site_code: str,
    site_id: str,
    region: str,
    environment: str,
    fields: Mapping[str, str],
) -> str:
    canonical = {
        "request_id": request_id,
        "site_code": site_code,
        "site_id": site_id,
        "region": region,
        "environment": environment,
        "fields": dict(sorted(fields.items())),
    }
    return hashlib.sha256(json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


class ToolWorkflow:
    """In-memory synthetic workflow; the only write target is its local draft ledger."""

    _site_code = re.compile(r"^[A-Z]\d{1,4}$")
    _allowed_fields = DRAFT_FIELDS

    def __init__(self, sites: dict[str, dict[str, str]]) -> None:
        self.sites = copy.deepcopy(sites)
        self.states: dict[str, str] = {}
        self.previews: dict[str, Preview] = {}
        self.prepared_by: dict[str, str] = {}
        self.approved_by: dict[str, str] = {}
        self.drafts: dict[str, dict[str, str]] = {}
        self.idempotency: dict[str, tuple[str, dict[str, str]]] = {}
        self.submitted_with: dict[str, str] = {}

    def lookup_site(self, site_code: str) -> dict[str, str]:
        """Perform an exact, read-only lookup; arbitrary queries are not accepted."""
        if not isinstance(site_code, str) or not self._site_code.fullmatch(site_code):
            raise ValueError("invalid site code")
        site = self.sites.get(site_code)
        if site is None:
            raise ValueError("unknown site")
        return {"site_id": site["site_id"], "region": site["region"]}

    def prepare(
        self, request_id: str, actor: Actor, site_code: str, fields: dict[str, str]
    ) -> Preview:
        if actor.role != "coordinator":
            raise AccessDenied("coordinator role required")
        if not isinstance(request_id, str) or not request_id.strip() or len(request_id) > 80:
            raise ValueError("invalid request id")
        site = self.lookup_site(site_code)
        if actor.region != site["region"]:
            raise AccessDenied("actor is outside the site region")
        if not isinstance(fields, dict) or fields.keys() - self._allowed_fields:
            raise ValueError("unsupported draft field")
        if any(not isinstance(value, str) or not value.strip() or len(value) > 280 for value in fields.values()):
            raise ValueError("invalid draft field value")
        if self.states.get(request_id) not in (None, "cancelled"):
            raise InvalidTransition("request already has an active workflow")

        self.approved_by.pop(request_id, None)
        self.submitted_with.pop(request_id, None)
        canonical = {
            "request_id": request_id,
            "site_code": site_code,
            "site_id": site["site_id"],
            "region": site["region"],
            "environment": "sandbox",
            "fields": dict(sorted(fields.items())),
        }
        preview_hash = _preview_digest(**canonical)
        preview = Preview(**canonical, preview_hash=preview_hash)
        self.previews[request_id] = preview
        self.prepared_by[request_id] = actor.subject
        self.states[request_id] = "pending_approval"
        return preview

    def approve(self, request_id: str, actor: Actor, preview_hash: str) -> None:
        preview = self._get_preview(request_id)
        if self.states.get(request_id) != "pending_approval":
            raise InvalidTransition("approval requires pending_approval state")
        if actor.role != "coordinator" or actor.region != preview.region:
            raise AccessDenied("coordinator is not authorized for this site")
        if actor.subject != self.prepared_by[request_id]:
            raise AccessDenied("approval must come from the request owner")
        if preview_hash != preview.preview_hash:
            raise InvalidTransition("preview changed; approval rejected")
        self.approved_by[request_id] = actor.subject
        self.states[request_id] = "approved"

    def submit(self, request_id: str, actor: Actor, idempotency_key: str) -> dict[str, str]:
        preview = self._get_preview(request_id)
        if actor.role != "coordinator" or actor.region != preview.region:
            raise AccessDenied("coordinator is not authorized for this site")
        approved_subject = self.approved_by.get(request_id)
        if approved_subject is None:
            raise InvalidTransition("approval required before submission")
        if approved_subject != actor.subject:
            raise AccessDenied("submission actor must own the approval")
        if not isinstance(idempotency_key, str) or not idempotency_key.strip():
            raise ValueError("idempotency key required")

        prior = self.idempotency.get(idempotency_key)
        if prior:
            prior_hash, prior_result = prior
            if prior_result.get("request_id") != request_id or prior_hash != preview.preview_hash:
                raise InvalidTransition("idempotency key reused with changed payload")
            if self.states.get(request_id) != "submitted" or self.submitted_with.get(request_id) != idempotency_key:
                raise InvalidTransition("idempotent replay requires the submitted workflow state")
            return dict(prior_result)
        if self.states.get(request_id) != "approved":
            raise InvalidTransition("approval required before submission")
        result = {"draft_id": f"draft-{len(self.drafts) + 1}", "request_id": request_id}
        self.drafts[request_id] = result
        self.idempotency[idempotency_key] = (preview.preview_hash, result)
        self.submitted_with[request_id] = idempotency_key
        self.states[request_id] = "submitted"
        return dict(result)

    def cancel(self, request_id: str, actor: Actor) -> None:
        preview = self._get_preview(request_id)
        if actor.role != "coordinator" or actor.region != preview.region:
            raise AccessDenied("coordinator is not authorized for this site")
        if actor.subject != self.prepared_by[request_id]:
            raise AccessDenied("only the request owner can cancel")
        if self.states.get(request_id) not in {"pending_approval", "approved"}:
            raise InvalidTransition("only an unsubmitted workflow can be cancelled")
        self.states[request_id] = "cancelled"
        self.approved_by.pop(request_id, None)

    def snapshot(self) -> dict[str, object]:
        return {
            "snapshot_version": 1,
            "states": dict(self.states),
            "previews": {
                key: {
                    "request_id": value.request_id,
                    "site_code": value.site_code,
                    "site_id": value.site_id,
                    "region": value.region,
                    "environment": value.environment,
                    "fields": dict(value.fields),
                    "preview_hash": value.preview_hash,
                }
                for key, value in self.previews.items()
            },
            "prepared_by": dict(self.prepared_by),
            "approved_by": dict(self.approved_by),
            "drafts": copy.deepcopy(self.drafts),
            "idempotency": copy.deepcopy(self.idempotency),
            "submitted_with": dict(self.submitted_with),
        }

    @classmethod
    def restore(cls, sites: dict[str, dict[str, str]], snapshot: dict[str, object]) -> ToolWorkflow:
        if not isinstance(snapshot, Mapping) or snapshot.get("snapshot_version") != 1:
            raise ValueError("unsupported workflow snapshot version")
        expected = {
            "snapshot_version", "states", "previews", "prepared_by", "approved_by",
            "drafts", "idempotency", "submitted_with",
        }
        if set(snapshot) != expected:
            raise ValueError("workflow snapshot has missing or unknown fields")
        workflow = cls(sites)
        states = snapshot["states"]
        previews = snapshot["previews"]
        prepared_by = snapshot["prepared_by"]
        approved_by = snapshot["approved_by"]
        drafts = snapshot["drafts"]
        idempotency = snapshot["idempotency"]
        submitted_with = snapshot["submitted_with"]
        if not all(isinstance(value, Mapping) for value in (states, previews, prepared_by, approved_by, drafts, idempotency, submitted_with)):
            raise ValueError("workflow snapshot maps are malformed")

        preview_fields = {
            "request_id", "site_code", "site_id", "region", "environment", "fields", "preview_hash"
        }
        for request_id, raw in previews.items():
            if not isinstance(request_id, str) or not isinstance(raw, Mapping) or set(raw) != preview_fields:
                raise ValueError("workflow snapshot preview is malformed")
            try:
                preview = Preview(**raw)
                site = workflow.lookup_site(preview.site_code)
            except (TypeError, ValueError, KeyError) as exc:
                raise ValueError("workflow snapshot preview is malformed") from exc
            if (
                preview.request_id != request_id
                or preview.site_id != site["site_id"]
                or preview.region != site["region"]
                or preview.environment != "sandbox"
                or _preview_digest(
                    preview.request_id,
                    preview.site_code,
                    preview.site_id,
                    preview.region,
                    preview.environment,
                    preview.fields,
                ) != preview.preview_hash
            ):
                raise ValueError("workflow snapshot preview integrity mismatch")
            workflow.previews[request_id] = preview

        workflow.states = dict(states)
        workflow.prepared_by = dict(prepared_by)
        workflow.approved_by = dict(approved_by)
        workflow.drafts = copy.deepcopy(dict(drafts))
        workflow.submitted_with = dict(submitted_with)
        if any(not isinstance(key, str) or not key.strip() for key in idempotency):
            raise ValueError("workflow snapshot idempotency key is malformed")
        workflow.idempotency = {}
        for key, entry in idempotency.items():
            if not isinstance(entry, (list, tuple)) or len(entry) != 2 or not isinstance(entry[0], str) or not isinstance(entry[1], Mapping):
                raise ValueError("workflow snapshot idempotency record is malformed")
            workflow.idempotency[key] = (entry[0], dict(entry[1]))

        workflow._validate_snapshot_state()
        return workflow

    def _validate_snapshot_state(self) -> None:
        request_ids = set(self.previews)
        if set(self.states) != request_ids or set(self.prepared_by) != request_ids:
            raise ValueError("workflow snapshot state does not match its previews")
        if any(
            not isinstance(request_id, str)
            or not isinstance(state, str)
            or not isinstance(self.prepared_by[request_id], str)
            or not self.prepared_by[request_id].strip()
            for request_id, state in self.states.items()
        ):
            raise ValueError("workflow snapshot state is malformed")
        allowed_states = {"pending_approval", "approved", "cancelled", "submitted"}
        if any(state not in allowed_states for state in self.states.values()):
            raise ValueError("workflow snapshot state is invalid")
        if any(request_id not in request_ids for request_id in self.approved_by):
            raise ValueError("workflow snapshot approval references an unknown request")
        for request_id, state in self.states.items():
            approval = self.approved_by.get(request_id)
            if state in {"approved", "submitted"}:
                if not isinstance(approval, str) or approval != self.prepared_by[request_id]:
                    raise ValueError("workflow snapshot approval state is inconsistent")
            elif approval is not None:
                raise ValueError("workflow snapshot approval state is inconsistent")

        submitted = {request_id for request_id, state in self.states.items() if state == "submitted"}
        if set(self.drafts) != submitted or set(self.submitted_with) != submitted:
            raise ValueError("workflow snapshot submission state is inconsistent")
        for request_id in submitted:
            result = self.drafts[request_id]
            if (
                not isinstance(result, Mapping)
                or set(result) != {"request_id", "draft_id"}
                or result.get("request_id") != request_id
                or not isinstance(result.get("draft_id"), str)
                or not re.fullmatch(r"draft-[1-9]\d*", result["draft_id"])
            ):
                raise ValueError("workflow snapshot draft record is malformed")
            key = self.submitted_with[request_id]
            record = self.idempotency.get(key)
            if record is None or record[1] != result or record[0] != self.previews[request_id].preview_hash:
                raise ValueError("workflow snapshot idempotency state is inconsistent")

        for _, (preview_hash, result) in self.idempotency.items():
            request_id = result.get("request_id")
            if (
                not isinstance(request_id, str)
                or request_id not in submitted
                or preview_hash != self.previews[request_id].preview_hash
                or self.submitted_with.get(request_id) not in self.idempotency
            ):
                raise ValueError("workflow snapshot idempotency state is inconsistent")

    def _get_preview(self, request_id: str) -> Preview:
        try:
            preview = self.previews[request_id]
        except KeyError as exc:
            raise InvalidTransition("workflow preview not found") from exc
        if preview.request_id != request_id or _preview_digest(
            preview.request_id,
            preview.site_code,
            preview.site_id,
            preview.region,
            preview.environment,
            preview.fields,
        ) != preview.preview_hash:
            raise InvalidTransition("preview integrity check failed; prepare and approve a new preview")
        return preview


T = TypeVar("T")


def retry_transient(operation: Callable[[], T], *, max_attempts: int = 3) -> T:
    """Retry only explicitly transient operations, with a finite attempt budget."""
    if max_attempts < 1:
        raise ValueError("max_attempts must be positive")
    for attempt in range(max_attempts):
        try:
            return operation()
        except TransientDependencyError:
            if attempt == max_attempts - 1:
                raise
    raise AssertionError("unreachable")
