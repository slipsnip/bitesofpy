from itertools import chain


STAR = '*'

def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    up = (1, width + 1, 2)
    down = (width - 2, 0, -2)
    num_stars = chain(range(*up), range(*down))    
    yield from ['{: ^{width}}'.format(STAR * count, width=width) for count in num_stars]