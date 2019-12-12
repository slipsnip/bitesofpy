from datetime import date

from dateutil import relativedelta
from dateutil.rrule import *

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    weekdays = rrule(DAILY, dtstart=start_date, wkst=MO, byweekday=range(0,5), count=100)
    return [day.date() for day in weekdays]