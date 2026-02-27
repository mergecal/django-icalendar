(usage)=

# Usage

`django-icalendar` provides Django ORM models for storing and exporting RFC 5545 iCalendar (`.ics`) data.

After {ref}`installing <installation>`, run migrations to create the required tables:

```bash
python manage.py migrate
```

See the individual model pages for usage examples:

- **CalendarModel** — store a VCALENDAR and export it as `.ics` bytes
- **EventModel** — store timed or all-day VEVENTs
- **AttendeeModel** — attach attendees to events
- **ConferenceModel** — attach conference links to events
