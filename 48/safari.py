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


def create_chart():
    data = defaultdict(str)
    with open(SAFARI_LOGS) as log:
        raw_data = ''
        pos = 0
        for line in log:
            if not line:
                continue
            raw_data += line.lower()
            if pos >= 1:
                fields = raw_data.split()
                pos = 0
                if not 'sending' in fields:
                    raw_data = ''
                    continue
                else:
                    date = fields[0]
                    if 'python' in raw_data:
                        data[date] += PY_BOOK
                    else:
                        data[date] += OTHER_BOOK
                raw_data = ''
            else:
                pos += 1
        for date, graph in data.items():
            print(f'{date} {graph}')