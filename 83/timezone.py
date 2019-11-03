from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    utc_dt = utc.localize(naive_utc_dt)
    aus = utc_dt.astimezone(AUSTRALIA)
    # aus = naive_utc_dt.astimezone(AUSTRALIA)
    # sp = naive_utc_dt.astimezone(SPAIN)
    # aus = AUSTRALIA.localize(utc_dt, is_dst=False)
    # aus = AUSTRALIA.localize(naive_utc_dt.astimezone(AUSTRALIA))
    # sp = SPAIN.localize(naive_utc_dt)
    sp = aus.astimezone(SPAIN)

    return (aus, sp)
