from string import ascii_lowercase
import re

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""


def slice_and_dice(text: str = text) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    results = []
    regex_non_alpha = r'^[^a-zA-Z]'
    cleaned_text = [line.strip() for line in text.splitlines()]
    for line in cleaned_text:
        if len(line) == 0:
            continue
        first_char = line[0]
        # ignore lines that do not begin with a letter
        if re.match(regex_non_alpha, line) != None:
            continue
        # check first character against its lowercase counterpart
        if first_char == first_char.lower():
            last_word = line.split()[-1]
            # remove any trailing ! or .
            last_word = re.sub(r'([!\.])$','',last_word)
            results.append(last_word)
    return results
