import re


def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    # get rid of pesky whitespace and blank lines
    striped = re.sub(r'\n+', r' ', text.strip())
    sentences = []
    for sentence in re.findall(r'([A-Z].+?[\.\?\!])(?=(\s[A-Z])|$)', striped):
        sentences.append(sentence[0])
    return sentences
