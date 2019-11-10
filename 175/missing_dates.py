import pandas
from datetime import date


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    # pandas series lets us sort by values and aparently suports dates
    sorted_dates = pandas.Series(dates).sort_values()
    # get first and last date from sorted to generate full range
    full_range = pandas.date_range(sorted_dates.iloc[0], sorted_dates.iloc[-1])
    return [date.date() for date in full_range if date.date() not in dates]