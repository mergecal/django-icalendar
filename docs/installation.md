(installation)=

# Installation

The package is published on [PyPI](https://pypi.org/project/django-icalendar/) and can be installed with `pip` (or any equivalent):

```bash
pip install django-icalendar
```

Add the app to your `INSTALLED_APPS` and ensure `USE_TZ` is enabled:

```python
INSTALLED_APPS = [
    # ...
    "django_icalendar",
]

USE_TZ = True  # required
```

The app will raise `ImproperlyConfigured` at startup if `USE_TZ` is not `True`.

## Why is `USE_TZ = True` required?

Without it, Django stores naive datetimes (no timezone info). When exporting
to `.ics`, the library converts stored datetimes to the requested timezone via
`astimezone()`. On a naive datetime, Python silently assumes the **server's
local timezone** as the source — no error is raised, but the exported
`DTSTART` will be wrong for any server not in the same timezone as your users.

With `USE_TZ = True`, Django normalises all datetimes to UTC on save, so
`astimezone()` always has an unambiguous source to convert from.
