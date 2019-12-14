from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    num_days = timedelta(days=num_days)
    current_date = start_date
    while(True):
        current_date += num_days
        for _ in range(num_bites):
            yield current_date

