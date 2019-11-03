from difflib import (SequenceMatcher, get_close_matches)
from os import path
from urllib.request import urlretrieve
from collections import namedtuple
from operator import attrgetter


DICTIONARY = path.join('/tmp', 'dictionary.txt')
if not path.isfile(DICTIONARY):
    urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)


def load_words():
    """Return a set of words from DICTIONARY"""
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines()}


def suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()
    ScoredWord = namedtuple('ScoredWord', 'word score')
    sm = SequenceMatcher()
    sm.set_seq2(misspelled_word)

    sugestions = get_close_matches(misspelled_word, words, n=5, cutoff=0.6)
    # SequenceMatcher.set_seq1() always returns None thus always succeeds, gets executed
    scored_sugestions = [ScoredWord(sugestion, sm.ratio()) for sugestion in sugestions if not sm.set_seq1(sugestion)]
    return max(scored_sugestions, key=attrgetter('score')).word 



    # you code