# Synthetic evaluation fixture

`evaluation.jsonl` contains eight original, fictional examples created for the Phase 2 exercises. It does not reproduce or claim to represent Meridian Facilities' real messages or any real person's information.

## Fields

- `case_id`: stable synthetic case identifier.
- `text`: fictional maintenance request.
- `expected_category`, `expected_location`, `expected_urgency`: expected outputs for the deterministic teaching baseline.
- `expected_missing_fields`: fields the baseline should leave unresolved.

## Coverage and limitations

The fixture covers clear routine/urgent/emergency phrases, missing location, vague requests, a benign “smoke detector” mention, and conflicting categories. Eight examples are enough to exercise these code paths, not to estimate real-world accuracy, prevalence, or operational impact. Add cases with an explicit rationale and update this card when the fixture changes.

All examples are synthetic and authored for this project. No third-party dataset is included.
