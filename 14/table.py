import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(names, *columns):
    yield from [SEPARATOR.join(str(column) for column in tuple) for tuple in zip(names,*columns)]