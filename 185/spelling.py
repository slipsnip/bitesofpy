from difflib import get_close_matches
from string import ascii_letters
from os import path
from urllib.request import urlretrieve


DICTIONARY = path.join('/tmp', 'dictionary.txt')
if not path.isfile(DICTIONARY):
    urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)


def load_words(startswith=None, min_len=1, cutoff=26):
    """Generator that yields words from DICTIONARY with
    optional restrictions

    :param startswith: Limit words that startwith this letter
    :type startswith: str
    :param min_len: Minumum length a word must be to be yielded
    :type min_len: int
    :param cutoff: Only yield words whose second letter is within cutoff chars of alphabet
    :type cutoff: int
    :return: Word from DICTIONARY within limits given
    :rtype: str
    
    """
    with open(DICTIONARY) as f:
        word = f.readline().lower().strip()
        # test if startswith is defined and weather word.startswith is true
        # if not defined continue with testing
        startswith = word.startswith(startswith) if startswith else True
        if startswith and len(word) > min_len and word[1] in ascii_letters[:cutoff]:
            yield word


def suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()

    return get_close_matches(misspelled_word, words, n=1, cutoff=0.6)[0]