(usage)=

# Usage

After {ref}`installing <installation>`, run migrations:

```bash
python manage.py migrate
```

## CalendarModel

Create a calendar and generate `.ics` bytes:

```{doctest}
>>> from django_icalendar.models import CalendarModel
>>> cal = CalendarModel(name="My Calendar")
>>> b"BEGIN:VCALENDAR" in cal.to_ical()
True
>>> b"NAME:My Calendar" in cal.to_ical()
True
```

Set optional fields — `color`, `method`, `description`, and `prodid` are all optional:

```{doctest}
>>> cal = CalendarModel(name="My Calendar", color="tomato", method="PUBLISH")
>>> b"COLOR:tomato" in cal.to_ical()
True
>>> b"METHOD:PUBLISH" in cal.to_ical()
True
```

Serve from a Django view:

```python
from django.http import HttpResponse
from django_icalendar.models import CalendarModel


def calendar_feed(request, pk):
    cal = CalendarModel.objects.get(pk=pk)
    return HttpResponse(cal.to_ical(), content_type="text/calendar")
```
