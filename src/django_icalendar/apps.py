from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangoIcalendarAppConfig(AppConfig):
    """App config for Django icalendar."""

    name = "django_icalendar"
    verbose_name = _("icalendar")
