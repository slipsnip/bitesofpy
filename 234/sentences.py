import re


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    sentences = [sentence.strip() for sentence in re.split(r'(?<=[\.\!\?]) |$', text)]
    return ' '.join(sentence[0].upper() + sentence[1:] for sentence in sentences if len(sentence) > 0)