from __future__ import annotations

import re

from meridian_intake.models import Category, IntakeRequest, IntakeSuggestion, Urgency


LOCATION_PATTERN = re.compile(r"\b(?:building|bldg)\s+([A-Z]?-?\d{1,4})\b", re.IGNORECASE)
CATEGORY_TERMS: tuple[tuple[Category, tuple[str, ...]], ...] = (
    (Category.ELECTRICAL, ("outlet", "breaker", "wiring", "light fixture")),
    (Category.HVAC, ("air conditioner", "hvac", "no heat", "thermostat")),
    (Category.PLUMBING, ("sink", "pipe", "plumbing leak", "active leak", "drain", "toilet")),
)
EMERGENCY_PHRASES = ("visible fire", "smell of gas", "sparking outlet", "outlet is sparking")
URGENT_PHRASES = ("active leak", "no heat", "no running water")


class RuleBasedProvider:
    """Small deterministic baseline; every result remains subject to human review."""

    def extract(self, request: IntakeRequest) -> IntakeSuggestion:
        text = " ".join(request.text.split())
        lowered = text.casefold()
        location_match = LOCATION_PATTERN.search(text)
        location = f"Building {location_match.group(1)}" if location_match else None

        matched_category = Category.UNKNOWN
        evidence: list[str] = []
        for category, terms in CATEGORY_TERMS:
            matching_terms = [term for term in terms if term in lowered]
            if matching_terms:
                if matched_category is not Category.UNKNOWN and matched_category is not category:
                    matched_category = Category.UNKNOWN
                    evidence = []
                    break
                matched_category = category
                evidence.extend(matching_terms)

        if any(phrase in lowered for phrase in EMERGENCY_PHRASES):
            urgency = Urgency.EMERGENCY
            evidence.extend(phrase for phrase in EMERGENCY_PHRASES if phrase in lowered)
        elif any(phrase in lowered for phrase in URGENT_PHRASES):
            urgency = Urgency.URGENT
            evidence.extend(phrase for phrase in URGENT_PHRASES if phrase in lowered)
        elif any(word in lowered for word in ("routine inspection", "replace filter", "schedule maintenance")):
            urgency = Urgency.ROUTINE
        else:
            urgency = Urgency.UNKNOWN

        missing: list[str] = []
        if location is None:
            missing.append("location")
        if matched_category is Category.UNKNOWN:
            missing.append("category")
        if urgency is Urgency.UNKNOWN:
            missing.append("urgency")

        return IntakeSuggestion(
            category=matched_category,
            location=location,
            urgency=urgency,
            summary=text[:280],
            missing_fields=missing,
            evidence=evidence,
            review_required=True,
        )
