from collections import namedtuple
from itertools import chain, repeat, product

"""There are 108 cards in a Uno deck. There are four suits, Red, Green, Yellow and Blue,
each consisting of one 0 card, two 1 cards, two 2s, 3s, 4s, 5s, 6s, 7s, 8s and 9s; 
    two Draw Two cards; two Skip cards; and two Reverse cards.
In addition there are four Wild cards and four Wild Draw Four cards."""

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    cards = [UnoCard(suit, face) for suit, face in product(SUITS, [0])]
    two_of = chain(range(1, 10), 'Draw Two,Skip,Reverse'.split(','))
    cards.extend(UnoCard(suit, face) for suit, face in product(SUITS, two_of) for _ in range(2))
    four_of = 'Wild,Wild Draw Four'.split(',')
    cards.extend(UnoCard(None, face) for _ in range(4) for face in four_of)
    return cards