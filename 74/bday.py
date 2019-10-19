from calendar import Calendar
from datetime import date
import re


WEEKDAYS = ("Monday \
                Tuesday \
                Wednesday \
                Thursday \
                Friday \
                Saturday \
                Sunday".split())

def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    cal = Calendar()

    weekday_lookup = dict(
        (day_number, day) for day_number, day in enumerate(WEEKDAYS))

    return [
        weekday_lookup[day_of_week]
        for day_of_month, day_of_week in cal.itermonthdays2(date.year, date.month)
        if day_of_month == date.day
    ][0]

if __name__ == '__main__':
    while(True):
        bday = input('When were you born? [YYYY-MM-DD]: ')
        valid_input = r'^\d{4}-\d{2}-\d{2}$'
        # if valid input break out of loop
        if re.match(valid_input, bday):
            break
    bday = date.fromisoformat(bday)
    weekday = weekday_of_birth_date(bday)
    print(f'You were born on a {weekday}')
