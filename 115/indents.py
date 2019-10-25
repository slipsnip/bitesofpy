import re


def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    return re.match(r'^[ ]*', text).end()


