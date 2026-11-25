from __future__ import annotations

from fastapi import FastAPI, HTTPException

from meridian_intake.baseline import RuleBasedProvider
from meridian_intake.models import IntakeRequest, IntakeSuggestion
from meridian_intake.providers import IntakeProvider, ProviderTimeout, ProviderUnavailable


def create_app(provider: IntakeProvider | None = None) -> FastAPI:
    selected_provider = provider or RuleBasedProvider()
    app = FastAPI(title="Meridian synthetic intake", version="0.1.0")

    @app.post("/v1/intake/suggestions", response_model=IntakeSuggestion)
    def suggest(request: IntakeRequest) -> IntakeSuggestion:
        try:
            return selected_provider.extract(request)
        except ProviderTimeout as exc:
            raise HTTPException(status_code=504, detail="suggestion provider timed out") from exc
        except ProviderUnavailable as exc:
            raise HTTPException(status_code=503, detail="suggestion provider unavailable") from exc

    return app


app = create_app()
