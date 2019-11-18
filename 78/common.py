from functools import reduce


def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    return reduce(lambda a, b: a & b, map(set, programmers.values()))