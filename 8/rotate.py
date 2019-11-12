"""Write a function that rotates characters in a string, in both directions:

if n is positive
    move characters from beginning to end, e.g.:
        rotate('hello', 2) would return llohe
if n is negative
    move characters to the start of the string, e.g.:
        rotate('hello', -2) would return lohel
"""


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    # default no change unless n is negative or positive
    rotated_string = string
    if n > 0:
        rotated_string = string[n:] + string[:n]
    elif n < 0:
        # calc how many letters remain after n characters are removed
        difference = len(string) - abs(n)
        # last n characters
        last_n = string[difference:]
        # remainder of string after n characters are chopped off end
        remainder_string = string[:difference]
        rotated_string = last_n + remainder_string
    return rotated_string
