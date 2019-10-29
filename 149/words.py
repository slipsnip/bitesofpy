def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case,
       one twist: numbers have to appear after letters!"""
    return sorted(words, key=lambda word: word.lower() if ord(word[0]) not in range(49,58) else chr(ord('z') + ord(word[0])))
 