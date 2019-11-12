import string

import pytest

from spelling import suggest_word, load_words


@pytest.fixture(scope='module')
def a_words():
    """Get only a[abcdefghijklm]-words to speed up tests"""
    return load_words(startswith='a', cutoff=13)

@pytest.mark.parametrize("word, expected", [
    ('acheive', 'achieve'),
    ('accross', 'across'),
    ('acceptible', 'acceptable'),
    ('allmost', 'almost'),
    ('aquire', 'acquire'),
    ('agressive', 'aggressive'),
    ('accomodate', 'accommodate'),
    ('accidentaly', 'accidentally'),
])
def test_suggest_word(word, expected, a_words):
    assert suggest_word(word, words=a_words) == expected