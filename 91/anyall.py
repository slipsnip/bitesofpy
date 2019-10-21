import re


VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    # use regex for this one
    vowels_found = re.findall(r'[aeiou]', input_str, flags=re.I)
    return len(vowels_found) == len(input_str)


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return any([True for char in input_str if char.upper() in PYTHON.upper()])


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return re.search(r'\d+', input_str)
