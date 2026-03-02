"""Tests for CalendarModel."""

import pytest
from icalendar import Calendar

from tests.factories import CalendarFactory

# ---------------------------------------------------------------------------
# Unit — __str__
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_str_returns_name():
    from django_icalendar.models import CalendarModel

    assert str(CalendarModel(name="My Cal")) == "My Cal"


# ---------------------------------------------------------------------------
# to_ical() — PRODID fallback chain
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_to_ical_model_prodid_takes_priority(settings):
    """Explicitly set prodid wins over settings and library default."""
    settings.ICALENDAR_PRODID = "-//Settings//EN"
    cal = CalendarFactory(prodid="-//Model//EN")
    parsed = Calendar.from_ical(cal.to_ical())
    assert str(parsed["PRODID"]) == "-//Model//EN"


@pytest.mark.django_db
def test_to_ical_settings_prodid_used_when_model_prodid_blank(settings):
    """When model prodid is blank, fall back to ICALENDAR_PRODID setting."""
    settings.ICALENDAR_PRODID = "-//Settings//EN"
    cal = CalendarFactory(prodid="")
    parsed = Calendar.from_ical(cal.to_ical())
    assert str(parsed["PRODID"]) == "-//Settings//EN"


@pytest.mark.django_db
def test_to_ical_library_default_prodid_when_nothing_set(settings):
    """When both model prodid and setting are absent, use the library default."""
    if hasattr(settings, "ICALENDAR_PRODID"):
        delattr(settings, "ICALENDAR_PRODID")
    cal = CalendarFactory(prodid="")
    parsed = Calendar.from_ical(cal.to_ical())
    assert "django-icalendar" in str(parsed["PRODID"])


# ---------------------------------------------------------------------------
# to_ical() — field mapping and empty-string handling
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_to_ical_empty_string_fields_omitted():
    """
    Fields stored as empty strings must not produce empty properties.
    Our ``field or None`` conversions guard against this.
    """
    cal = CalendarFactory(description="", color="", method="")
    output = cal.to_ical()
    parsed = Calendar.from_ical(output)
    assert parsed.get("COLOR") is None
    assert parsed.get("METHOD") is None


@pytest.mark.django_db
def test_to_ical_all_optional_fields_round_trip(db):
    """Every optional field that is set must appear in the output."""
    cal = CalendarFactory(
        description="A description",
        color="tomato",
        method="PUBLISH",
    )
    parsed = Calendar.from_ical(cal.to_ical())
    assert parsed.get("METHOD") is not None
    assert parsed.get("COLOR") is not None


@pytest.mark.django_db
def test_to_ical_returns_bytes(calendar):
    assert isinstance(calendar.to_ical(), bytes)


# ---------------------------------------------------------------------------
# Fixture comparison — golden-file regression tests
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_minimal_calendar_matches_fixture(db, assert_ical_match):
    """
    A calendar with only a name and default prodid must match the
    minimal fixture exactly.
    """
    cal = CalendarFactory(name="Minimal Calendar", prodid="")
    assert_ical_match(cal.to_ical(), "calendar_minimal.ics")


@pytest.mark.django_db
def test_full_calendar_matches_fixture(db, assert_ical_match):
    """
    A calendar with every optional field populated must match the
    full fixture exactly.
    """
    cal = CalendarFactory(
        name="Full Calendar",
        description="A full description",
        prodid="-//Custom//Custom//EN",
        color="tomato",
        method="PUBLISH",
    )
    assert_ical_match(cal.to_ical(), "calendar_full.ics")
