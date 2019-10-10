from secrets import choice
from string import ascii_uppercase
from string import digits
def gen_key(parts=4, chars_per_part=8):
    valid_chars = ascii_uppercase + digits
    key = ''
    for index in range(1, parts + 1):
        part = ''.join(choice(valid_chars) for count in range(chars_per_part))
        key += (part, part + '-')[index < parts]
    return key
