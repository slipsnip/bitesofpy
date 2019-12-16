import os
import re
from collections import namedtuple
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
    data_ = re.compile(r'^(\d{2}-\d{2}).+?-\s(.+)') 
    try:
        return LINE(*data_.match(line).groups())
    except:
        return None


def create_chart():
    lines = []
    date_prev = ''
    is_first_run = True
    bar = ''
    with open(SAFARI_LOGS) as log:
        bar = ''
        for line in log.readlines():
            line = parse_(line)
            lines.append(line)
            if not line:
                continue
            if line.date != date_prev:
                if bar:
                    print(out + bar)
                    bar = ''
                out = line.date + ' '
                date_prev = line.date
                is_new_date = True
            else:
                is_new_date = False
            if 'sending' in line.msg.split():
                if 'python' in lines[-2].msg.lower().split():
                    bar += PY_BOOK
                else:
                    bar += OTHER_BOOK
        print(out + bar)


