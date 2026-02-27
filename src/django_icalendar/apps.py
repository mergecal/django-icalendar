from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _


class DjangoIcalendarAppConfig(AppConfig):
    """App config for django-icalendar."""

    name = "django_icalendar"
    verbose_name = _("icalendar")
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self) -> None:
        """Validate required Django settings on startup."""
        if not getattr(settings, "USE_TZ", False):
            raise ImproperlyConfigured(
                "django-icalendar requires USE_TZ=True in your Django settings."
            )
