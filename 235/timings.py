from pathlib import Path
from urllib.request import urlretrieve
from operator import (itemgetter, attrgetter)
from dataclasses import (dataclass, field)
from typing import Tuple

tmp = Path('/tmp')
timings_log = tmp / 'pytest_timings.out'
if not timings_log.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )


# PytestResult = namedtuple('PytestResult', 'byte num_passed total_seconds passed')

@dataclass
class PytestResult(object):
    byte: int
    num_tests: int
    total_seconds: float = field(metadata={'unit': 'seconds'})
    passed: bool = field(default=False)
    average: float = field(init=False)
    # sort_index: int = field(init=False, repr=False)


    def __post_init__(self):
        if self.passed:
            self.average = self.total_seconds / self.num_tests
            # self.sort_index = float(self.average)
        else:
            self.average = float('inf')
            # self.sort_index = float('inf')
    
    def __lt__(self, rhs):
        return self.average < rhs.average


def parse_pytest_string(record: str) -> Tuple[int]:
    fields = record.split()
    byte, num_tests, total_seconds = itemgetter(0, 2, -3)(fields)
    byte = int(byte)
    total_seconds = float(total_seconds)
    if not num_tests.isnumeric():
        return (byte, 0, 0.00) 
    elif 'passed' not in fields:
        return (byte, int(num_tests), total_seconds)
    else:
        return (byte, int(num_tests), total_seconds, True)

def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    # if index 2 of test result isnumeric passed is True, thus use as bool for passed
    results = [PytestResult(*parse_pytest_string(record)) for record in timings]
    fastest = min(results)
    return fastest.byte