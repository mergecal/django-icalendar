import pytest
from django.core.exceptions import ImproperlyConfigured


def test_use_tz_required(settings):
    """App raises ImproperlyConfigured when USE_TZ is False."""
    settings.USE_TZ = False
    from django_icalendar.apps import DjangoIcalendarAppConfig

    app = DjangoIcalendarAppConfig("django_icalendar", __import__("django_icalendar"))
    with pytest.raises(ImproperlyConfigured, match="USE_TZ"):
        app.ready()


def test_use_tz_passes(settings):
    """App starts normally when USE_TZ is True."""
    settings.USE_TZ = True
    from django_icalendar.apps import DjangoIcalendarAppConfig

    app = DjangoIcalendarAppConfig("django_icalendar", __import__("django_icalendar"))
    app.ready()  # should not raise
