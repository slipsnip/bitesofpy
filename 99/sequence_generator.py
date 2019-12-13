from string import ascii_uppercase, digits
from itertools import cycle


def sequence_generator():
    sequence = cycle(element for pair in zip(range(1, 27), ascii_uppercase) for element in pair)
    yield from sequence