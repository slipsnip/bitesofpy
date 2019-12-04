from collections import OrderedDict
from itertools import takewhile

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):
    ranks = list(takewhile(lambda score: user_score >= score, HONORS))
    if not ranks:
        return None if len(ranks) == 0 else 'red'
    return HONORS[ranks[-1]]
