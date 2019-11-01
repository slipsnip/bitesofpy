from string import ascii_letters
from collections import defaultdict

PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    char_table = defaultdict(str)
    for letter in ascii_letters:
        char_table[letter] = letter.swapcase() if letter.lower() in 'pybites' else letter
    trans_table = str.maketrans(dict(char_table))
    return text.translate(trans_table)


def convert_pybites_chars_simple(text):
    return ''.join(char.swapcase() if char.lower() in 'pybites' else char for char in text)
