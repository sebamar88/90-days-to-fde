from __future__ import annotations

from typing import Protocol

from meridian_intake.models import IntakeRequest, IntakeSuggestion


class ProviderTimeout(Exception):
    """The provider did not return before the caller's deadline."""


class ProviderUnavailable(Exception):
    """The provider cannot currently serve the request."""


class IntakeProvider(Protocol):
    def extract(self, request: IntakeRequest) -> IntakeSuggestion:
        """Return a validated suggestion; this operation must not perform writes."""
