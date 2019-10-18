import re


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    punctuation = re.compile(r'[!"#$%&\'()*\\+,-./:;<=>?@\[\]^_`{|}]')
    return re.sub(punctuation, '', input_string)
