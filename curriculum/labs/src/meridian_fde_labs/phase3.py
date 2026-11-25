"""Bounded tools and approval-gated workflow used by the Phase 3 lab."""

from __future__ import annotations

import copy
import hashlib
import json
import re
from dataclasses import asdict, dataclass
from typing import Callable, TypeVar


class AccessDenied(PermissionError):
    """The trusted actor context does not permit the requested operation."""


class InvalidTransition(ValueError):
    """The requested state transition is not valid for this workflow."""


class TransientDependencyError(RuntimeError):
    """A dependency may recover and the read-only operation may be retried."""


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
    fields: dict[str, str]
    preview_hash: str


class ToolWorkflow:
    """In-memory synthetic workflow; the only write target is its local draft ledger."""

    _site_code = re.compile(r"^[A-Z]\d{1,4}$")
    _allowed_fields = {"category", "urgency", "summary"}

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

        canonical = {
            "request_id": request_id,
            "site_code": site_code,
            "site_id": site["site_id"],
            "region": site["region"],
            "environment": "sandbox",
            "fields": dict(sorted(fields.items())),
        }
        preview_hash = hashlib.sha256(
            json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
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
            if prior_hash != preview.preview_hash:
                raise InvalidTransition("idempotency key reused with changed payload")
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

    def snapshot(self) -> dict[str, object]:
        return {
            "states": dict(self.states),
            "previews": {key: asdict(value) for key, value in self.previews.items()},
            "prepared_by": dict(self.prepared_by),
            "approved_by": dict(self.approved_by),
            "drafts": copy.deepcopy(self.drafts),
            "idempotency": copy.deepcopy(self.idempotency),
            "submitted_with": dict(self.submitted_with),
        }

    @classmethod
    def restore(cls, sites: dict[str, dict[str, str]], snapshot: dict[str, object]) -> ToolWorkflow:
        workflow = cls(sites)
        workflow.states = dict(snapshot["states"])
        workflow.previews = {
            key: Preview(**value) for key, value in dict(snapshot["previews"]).items()
        }
        workflow.prepared_by = dict(snapshot["prepared_by"])
        workflow.approved_by = dict(snapshot["approved_by"])
        workflow.drafts = copy.deepcopy(snapshot["drafts"])
        workflow.idempotency = copy.deepcopy(snapshot["idempotency"])
        workflow.submitted_with = dict(snapshot["submitted_with"])
        return workflow

    def _get_preview(self, request_id: str) -> Preview:
        try:
            return self.previews[request_id]
        except KeyError as exc:
            raise InvalidTransition("workflow preview not found") from exc


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
