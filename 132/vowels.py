from operator import itemgetter

VOWELS = list('aeiou')


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    vowel_counts = [(word, sum(word.count(vowel) for vowel in VOWELS)) for word in text.split()]
    return max(vowel_counts, key=itemgetter(1))