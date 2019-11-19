from random import choice

COLORS = "red blue green yellow brown purple".split()


class EggCreator:
    def __init__(self, limit):
        self._limit = limit
        self._count = 0  #  keep track of how many eggs

    def __next__(self):
        if self._count != self._limit:
            self._count += 1
            return f"{choice(COLORS)} egg"
        else:
            raise StopIteration

    def __iter__(self):
        return self
