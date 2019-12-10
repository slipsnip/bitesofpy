from unicodedata import name


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return  ''.join(letter for letter in text.lower() if 'WITH' in name(letter))