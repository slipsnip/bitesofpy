from datetime import datetime, timedelta
from collections import defaultdict
from string import ascii_lowercase
import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    param_lookup = dict(d='days',h='hours',m='minutes',s='seconds')
    if delay_time[-1] not in ascii_lowercase:
        delay_time += 's'
    parts = delay_time.split(' ')
    arguments = dict((param_lookup.get(part[-1]), int(part[:-1])) for part in parts)
    when = (start_time + timedelta(**arguments)).strftime('%Y-%m-%d %H:%M:%S')
    return f"{task} @ {when}"

    