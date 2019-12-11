from re import sub as substitute
from functools import partial


def is_anagram(*words):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    word1, word2 = map(partial(substitute, r'\s', r''), [word.lower() for word in words])
    return set(word1) ^ set(word2) == set() and \
        len(word1) == len(word2)
