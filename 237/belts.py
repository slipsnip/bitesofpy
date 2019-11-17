import json
from pathlib import Path
from dateutil.parser import parse
from datetime import date
from collections import defaultdict
from itertools import takewhile

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS = ('white yellow orange green blue brown black '
         'paneled red').split()
TMP = Path('/tmp')


def get_belts(data: str) -> dict:
    """Parsed the passed in json data:
       {"date":"5/1/2019","score":1},
       {"date":"9/13/2018","score":3},
       {"date":"10/25/2019","score":1},

       Loop through the scores in chronological order,
       determining when belts were achieved (use SCORES
       and BELTS).

       Return a dict with keys = belts, and values =
       readable dates, example entry:
       'yellow': 'January 25, 2018'
    """
    belt_scores = dict(zip(SCORES, BELTS))
    
    with open(data) as data_fd:
        data = json.load(data_fd)
    ordered = sorted(data, key=lambda day: parse(day['date']).date())
    belts_earned = defaultdict(date)
    total_score = 0

    for record in ordered:

        total_score += record['score']
        # list of scores surpassed, last element will be current_level
        scores_ = list(takewhile(lambda score: total_score >= score, SCORES))
        if scores_:
            level_ = scores_[-1]
            belt = belt_scores[level_]
            if belt in belts_earned.keys():
                continue
            belts_earned[belt] = parse(record['date']).strftime('%B %d, %Y')
    return dict(belts_earned)

    

     