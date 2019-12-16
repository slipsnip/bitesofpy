import os
import re
from collections import namedtuple, defaultdict
import urllib.request



TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'
LINE = namedtuple('Line', 'date msg')

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)

def parse_(line):
    if not line:
        return None
    choped_line = line.lower().split()
    if 'python' in choped_line:
        msg = PY_BOOK
    elif 'sending' in choped_line:
        msg = 'sending'
    elif 'skipping' in choped_line:
        msg = 'skipping'
    else:
        msg = OTHER_BOOK
        
    return LINE(choped_line[0], msg)


def create_chart():
    data = defaultdict(str)
    with open(SAFARI_LOGS) as log:
        lines = [parse_(line) for line in log.readlines()]
        for index, line in enumerate(lines):
            if line.msg == 'sending':
                previous_line = lines[index - 1]
                data[previous_line.date] += previous_line.msg
        for date, graph in data.items():
            print(f'{date} {graph}')




