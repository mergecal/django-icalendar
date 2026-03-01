"""factory_boy factories for django-icalendar models."""

import factory

from django_icalendar.models import CalendarModel


class CalendarFactory(factory.django.DjangoModelFactory):
    """Factory for CalendarModel."""

    name = factory.Sequence(lambda n: f"Test Calendar {n}")

    class Meta:
        """Factory meta options."""

        model = CalendarModel
