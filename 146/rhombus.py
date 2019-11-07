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
    up = range(1, width + 1, 2) if width % 2 != 0 else range(1, width, 2)
    down = up[:-1][::-1]  # ignore last element of up and reverse sequence
    num_stars = chain(up, down)    
    yield from ['{: ^{width}}'.format(STAR * count, width=width) for count in num_stars]