from collections import namedtuple
from functools import reduce

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


def calculate_score(scores):
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    # if any(score not in DICE_VALUES for score in scores)
    # return sum(score for score in scores if score >= MIN_SCORE)
    total = 0
    for score in scores:
        if score not in DICE_VALUES:
            raise ValueError
        total += score if score >= MIN_SCORE else 0
    return total
        

def get_winner(players):
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.

       If the length of the scores lists of the players passed in
       don't match up raise a ValueError.

       Returns a Player namedtuple of the winner.
       You can assume there is only one winner.

       For example - input:
         Player(name='player 1', scores=[1, 3, 2, 5])
         Player(name='player 2', scores=[1, 1, 1, 1])
         Player(name='player 3', scores=[4, 5, 1, 2])

       output:
         Player(name='player 3', scores=[4, 5, 1, 2])
    """
    winner = players[0]  # keep track of current winner, first player unless proven otherwise
    previous_ = players[0] # keep track of previous player processed
    for player in players:
        if len(player.scores) != len(previous_.scores):
            raise ValueError
        winner = player if calculate_score(player.scores) > calculate_score(previous_.scores) else winner
    return winner