"""Shared pytest fixtures and assertion helpers."""

from pathlib import Path

import pytest
from icalendar import Calendar

from tests.factories import CalendarFactory

FIXTURES_DIR = Path(__file__).parent / "fixtures" / "ics"


@pytest.fixture()
def calendar(db):
    """A minimal saved CalendarModel instance."""
    return CalendarFactory()


@pytest.fixture()
def assert_ical_match():
    """Return the assert_ical_match helper bound to the fixtures directory."""
    return _assert_ical_match


def _assert_ical_match(output: bytes, fixture_name: str) -> None:
    """
    Assert that *output* is semantically equal to the named ``.ics`` fixture.

    Reads ``tests/fixtures/ics/<fixture_name>``, parses both it and *output*
    with ``Calendar.from_ical``, then checks that every property present in
    the fixture exists in the actual output with the same value.

    Comparison is semantic rather than byte-for-byte, so changes in
    line-folding or property ordering in the icalendar library do not cause
    false failures.
    """
    fixture_path = FIXTURES_DIR / fixture_name
    expected = Calendar.from_ical(fixture_path.read_bytes())
    actual = Calendar.from_ical(output)

    for prop, expected_value in expected.items():
        actual_value = actual.get(prop)
        assert actual_value is not None, f"Property {prop!r} missing from output"
        assert str(actual_value) == str(expected_value), (
            f"Property {prop!r}: expected {expected_value!r}, got {actual_value!r}"
        )
