Configuration
=============

``ICALENDAR_PRODID``
--------------------

The ``PRODID`` property identifies the software that generated the calendar.
Defaults to ``-//django-icalendar//django-icalendar//EN`` if not set.

.. code-block:: python

    # settings.py
    ICALENDAR_PRODID = "-//My App//My App//EN"
