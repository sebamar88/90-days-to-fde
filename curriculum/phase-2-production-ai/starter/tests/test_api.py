import pytest
from fastapi import HTTPException
from pydantic import ValidationError

from meridian_intake.app import create_app
from meridian_intake.baseline import RuleBasedProvider
from meridian_intake.models import IntakeRequest, IntakeSuggestion
from meridian_intake.providers import ProviderTimeout, ProviderUnavailable


class FixedProvider:
    def extract(self, request: IntakeRequest) -> IntakeSuggestion:
        return RuleBasedProvider().extract(request)


class TimeoutProvider:
    def extract(self, request: IntakeRequest) -> IntakeSuggestion:
        raise ProviderTimeout


class UnavailableProvider:
    def extract(self, request: IntakeRequest) -> IntakeSuggestion:
        raise ProviderUnavailable


class InvalidOutputProvider:
    def extract(self, request: IntakeRequest) -> IntakeSuggestion:
        return {"category": "made-up", "review_required": False}  # type: ignore[return-value]


class SpyProvider(FixedProvider):
    def __init__(self) -> None:
        self.calls = 0

    def extract(self, request: IntakeRequest) -> IntakeSuggestion:
        self.calls += 1
        return super().extract(request)


def invoke_suggestion(provider, payload: dict[str, str]):
    app = create_app(provider)
    route = next(route for route in app.routes if getattr(route, "path", None) == "/v1/intake/suggestions")
    request = IntakeRequest.model_validate(payload)
    return route.endpoint(request)


def test_suggestion_endpoint_uses_injected_provider() -> None:
    result = invoke_suggestion(
        FixedProvider(), {"request_id": "demo-1", "text": "Building 12: active leak under the sink."}
    )

    assert result.review_required is True
    assert result.location == "Building 12"


def test_provider_timeout_is_explicit() -> None:
    with pytest.raises(HTTPException) as error:
        invoke_suggestion(
            TimeoutProvider(),
            {"request_id": "demo-2", "text": "Routine filter replacement in Building 8."},
        )

    assert error.value.status_code == 504


def test_provider_unavailable_is_explicit() -> None:
    with pytest.raises(HTTPException) as error:
        invoke_suggestion(
            UnavailableProvider(),
            {"request_id": "demo-unavailable", "text": "Routine filter replacement in Building 8."},
        )

    assert error.value.status_code == 503
    assert error.value.detail == "suggestion provider unavailable"


def test_invalid_provider_output_is_rejected() -> None:
    with pytest.raises(HTTPException) as error:
        invoke_suggestion(
            InvalidOutputProvider(),
            {"request_id": "demo-invalid", "text": "Routine filter replacement in Building 8."},
        )

    assert error.value.status_code == 502
    assert error.value.detail == "suggestion provider returned invalid output"


def test_invalid_request_is_rejected_before_provider_call() -> None:
    provider = SpyProvider()
    with pytest.raises(ValidationError):
        invoke_suggestion(provider, {"request_id": "demo-3", "text": "   "})

    assert provider.calls == 0
