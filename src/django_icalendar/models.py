"""Django models for storing iCalendar data."""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from icalendar import Calendar


class CalendarModel(models.Model):
    """
    Stores a VCALENDAR component.

    Call :meth:`to_ical` to generate RFC 5545-compliant ``.ics`` bytes.
    """

    name = models.CharField(_("name"), max_length=255)
    """Display name of the calendar (``NAME`` / ``X-WR-CALNAME``)."""

    description = models.TextField(_("description"), blank=True)
    """Optional long description (``DESCRIPTION`` / ``X-WR-CALDESC``)."""

    prodid = models.CharField(
        _("product ID"),
        max_length=255,
        blank=True,
        help_text=_(
            "Falls back to settings.ICALENDAR_PRODID or "
            "'-//django-icalendar//django-icalendar//EN'."
        ),
    )
    """``PRODID`` value. Falls back to ``settings.ICALENDAR_PRODID``
    or ``-//django-icalendar//django-icalendar//EN`` when blank."""

    color = models.CharField(
        _("color"),
        max_length=50,
        blank=True,
        help_text=_("CSS3 color name or hex value, e.g. 'tomato' or '#FF6347'."),
    )
    """CSS3 color name or hex value emitted as the ``COLOR`` property
    (RFC 7986), e.g. ``"tomato"`` or ``"#FF6347"``."""

    method = models.CharField(
        _("method"),
        max_length=30,
        blank=True,
        help_text=_("iTIP method (RFC 5546): PUBLISH, REQUEST, REPLY, etc."),
    )
    """iTIP method (RFC 5546) such as ``PUBLISH`` or ``REQUEST``.
    Leave blank to omit the ``METHOD`` property."""

    class Meta:
        """Database options for CalendarModel."""

        verbose_name = _("Calendar")
        verbose_name_plural = _("Calendars")

    def __str__(self) -> str:
        """Return the calendar name."""
        return self.name

    def to_ical(self) -> bytes:
        """Return RFC 5545-compliant ``.ics`` bytes for this calendar."""
        prodid = (
            self.prodid
            or getattr(settings, "ICALENDAR_PRODID", None)
            or "-//django-icalendar//django-icalendar//EN"
        )

        cal = Calendar.new(
            name=self.name or None,
            description=self.description or None,
            prodid=prodid,
            color=self.color or None,
            method=self.method or None,
        )

        return cal.to_ical()
