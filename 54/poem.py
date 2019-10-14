import re


INDENTS = 4


def print_hanging_indents(poem):
    poem_striped = poem.strip()
    poem_cleaned = re.sub(r'[ ]{2,}', r'', poem_striped)

    for paragraph in poem_cleaned.split('\n\n'):
        for line in enumerate(paragraph.split('\n')):
            if line[0] == 0:
                print(line[1])
            else:
                print(' ' * INDENTS + line[1])
