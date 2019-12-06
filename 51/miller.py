from datetime import datetime
from decimal import Decimal

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    delta_seconds = (PY2_DEATH_DT - start_date).total_seconds()
    delta_hours = delta_seconds / pow(60,2)
    return round(delta_hours, 2)

def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    # one hour = 7 earth years
    # 60 minutes = 7 earth years
    # 60 minutes = 60 * 24 * 365 * 7
    miller_constant = Decimal(60 / (60 * 24 * 365 * 7))
    delta_minutes = Decimal((PY2_DEATH_DT - start_date).total_seconds() / 60)
    return float((delta_minutes * miller_constant).quantize(Decimal('.01')))
