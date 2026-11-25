from fastapi.testclient import TestClient

from meridian_intake.app import create_app
from meridian_intake.baseline import RuleBasedProvider
from meridian_intake.models import IntakeRequest, IntakeSuggestion
from meridian_intake.providers import ProviderTimeout


class FixedProvider:
    def extract(self, request: IntakeRequest) -> IntakeSuggestion:
        return RuleBasedProvider().extract(request)


class TimeoutProvider:
    def extract(self, request: IntakeRequest) -> IntakeSuggestion:
        raise ProviderTimeout


def test_suggestion_endpoint_uses_injected_provider() -> None:
    client = TestClient(create_app(FixedProvider()))

    response = client.post(
        "/v1/intake/suggestions",
        json={"request_id": "demo-1", "text": "Building 12: active leak under the sink."},
    )

    assert response.status_code == 200
    assert response.json()["review_required"] is True
    assert response.json()["location"] == "Building 12"


def test_provider_timeout_is_explicit() -> None:
    client = TestClient(create_app(TimeoutProvider()))

    response = client.post(
        "/v1/intake/suggestions",
        json={"request_id": "demo-2", "text": "Routine filter replacement in Building 8."},
    )

    assert response.status_code == 504


def test_invalid_request_is_rejected_before_provider_call() -> None:
    client = TestClient(create_app(FixedProvider()))

    response = client.post("/v1/intake/suggestions", json={"request_id": "demo-3", "text": "   "})

    assert response.status_code == 422
