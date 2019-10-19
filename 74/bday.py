from calendar import Calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    cal = Calendar()

    weekdays = "Monday \
                Tuesday \
                Wednesday \
                Thursday \
                Friday \
                Saturday \
                Sunday".split()
    weekday_lookup = dict(
        (day_number, day) for day_number, day in enumerate(weekdays))

    return [
        weekday_lookup[day_of_week]
        for day_of_month, day_of_week in cal.itermonthdays2(date.year, date.month)
        if day_of_month == date.day
    ][0]
