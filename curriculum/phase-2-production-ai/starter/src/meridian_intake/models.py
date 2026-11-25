from __future__ import annotations

from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Category(StrEnum):
    ELECTRICAL = "electrical"
    HVAC = "hvac"
    PLUMBING = "plumbing"
    OTHER = "other"
    UNKNOWN = "unknown"


class Urgency(StrEnum):
    ROUTINE = "routine"
    URGENT = "urgent"
    EMERGENCY = "emergency"
    UNKNOWN = "unknown"


class IntakeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    request_id: str = Field(min_length=1, max_length=80)
    text: str = Field(min_length=1, max_length=8_000)


class IntakeSuggestion(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    category: Category
    location: str | None = Field(default=None, max_length=80)
    urgency: Urgency
    summary: str = Field(min_length=1, max_length=280)
    missing_fields: list[Literal["location", "category", "urgency"]] = Field(default_factory=list)
    evidence: list[str] = Field(default_factory=list, max_length=10)
    review_required: Literal[True] = True
