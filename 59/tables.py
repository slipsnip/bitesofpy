from itertools import product, repeat


class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._table = [[0] * length for height in range(length)]
        for y, x in product(range(1,length + 1), range(1, length +1)):
            self._table[y-1][x-1] = y * x
        self._area = length ** 2


    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return self._area

    def __str__(self):
        """Returns a string representation of the table"""
        out = [] 
        for row in self._table:
            out.append(' | '.join(str(value) for value in row))
        return '\n'.join(out)

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        return self._table[y-1][x-1]