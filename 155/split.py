import re


def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    # With regex split
    return [''.join(group) for group in re.findall(r'(?<=\")(.+)(?=\")|(\b\w+\b)', text)]  