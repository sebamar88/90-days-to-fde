from __future__ import annotations

import re
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[3]
CURRICULUM = REPOSITORY / "curriculum"
PHASE_TEST_PATHS = {
    1: "../labs/tests/test_phase1_discovery_packet.py",
    2: "../phase-2-production-ai/starter/tests/",
    3: "../labs/tests/test_phase3_workflow.py",
    4: "../labs/tests/test_phase4_evaluation_security.py",
    5: "../labs/tests/test_phase5_delivery.py",
    6: "../labs/tests/test_phase6_capstone.py",
}


def test_every_lesson_links_to_an_existing_phase_test_suite() -> None:
    lessons = sorted(CURRICULUM.glob("phase-*/day-*.md"))

    assert len(lessons) == 90
    for lesson in lessons:
        phase = int(re.search(r"phase-(\d+)-", lesson.parent.name).group(1))
        text = lesson.read_text(encoding="utf-8")
        section = text.split("## Automated lab", maxsplit=1)
        assert len(section) == 2, f"{lesson.relative_to(REPOSITORY)} lacks an automated lab section"
        target = PHASE_TEST_PATHS[phase]
        assert f"]({target})" in section[1], f"{lesson.relative_to(REPOSITORY)} links to the wrong test suite"
        assert (lesson.parent / target).resolve().exists(), f"{lesson.relative_to(REPOSITORY)} links to missing tests"


def test_every_phase_has_a_reference_lab_and_a_runnable_test_file() -> None:
    module_paths = {
        1: REPOSITORY / "curriculum/labs/src/meridian_fde_labs/phase1.py",
        2: REPOSITORY / "curriculum/phase-2-production-ai/starter/src/meridian_intake/app.py",
        3: REPOSITORY / "curriculum/labs/src/meridian_fde_labs/phase3.py",
        4: REPOSITORY / "curriculum/labs/src/meridian_fde_labs/phase4.py",
        5: REPOSITORY / "curriculum/labs/src/meridian_fde_labs/phase5.py",
        6: REPOSITORY / "curriculum/labs/src/meridian_fde_labs/phase6.py",
    }
    for phase, module in module_paths.items():
        assert module.is_file(), f"Phase {phase} reference lab is missing"
