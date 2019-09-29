from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)

"""Generator function that increments time by 5 day increments
    starting from PyBites date of founding: PYBITES_BORN
    yielding every date that is a multiple of 100 days or 365
    days, marking anniversaries"""
def gen_special_pybites_dates():
    # assume gregorian calendar
    # assume no leap year
    # 5 day incrementer; greatest common divisor of 365 days and 100 days
    time_delta_5_days = timedelta(days=5)
    # keep track of passage of time after each 5 day increments
    current_datetime_tracker = PYBITES_BORN
    while (current_datetime_tracker <= datetime.now()):
        current_datetime_tracker += time_delta_5_days
        days_passed = (current_datetime_tracker - PYBITES_BORN).days
        if (days_passed % 100 == 0):
            yield current_datetime_tracker
        elif (days_passed % 365 == 0):
            yield current_datetime_tracker


