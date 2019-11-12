from math import (floor, ceil)


def round_even(number):
    return (lambda num: (round(num), [val for val in (floor(num), ceil(num)) if
                                      val % 2 == 0][0])[num % 0.5 == 0])(number)
    # """Takes a number and returns it rounded even"""
    # if number % 0.5 != 0:
    #     return round(number)
    # else:
    #     return [value for value in
    #             (floor(number), ceil(number))
    #             if value % 2 == 0][0]
