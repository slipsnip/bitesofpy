from collections import namedtuple
from datetime import datetime, timedelta
from itertools import takewhile

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime) or \
        date > NOW:
            raise ValueError
    dx = int((NOW - date).total_seconds())
    before = lambda time_offset: dx < time_offset.offset
    time_offsets = list(takewhile(before, TIME_OFFSETS[::-1]))
    if time_offsets:
        time_offset = time_offsets[-1]
        return time_offset.date_str.format(dx // (time_offset.divider or 1))
    days = (NOW - date).days
    return (NOW - timedelta(days=days)).strftime('%m/%d/%y')
