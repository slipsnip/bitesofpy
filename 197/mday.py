from datetime import datetime
from dateutil.rrule import (rrule, SU, YEARLY)
from dateutil.parser import parse


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    start_date = parse(f"Jan {year}").date()
    for date in rrule(YEARLY, dtstart=start_date, bymonth=5, byweekday=SU, bysetpos=2):
        if date.year == year:
            return date.date()
