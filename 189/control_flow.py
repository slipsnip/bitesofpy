# names that start with IGNORE_CHAR are ignored,
# names that have one or more digits are ignored,
# if a name starts with QUIT_CHAR it inmediately exits the loop, so no more names are added/generated at this point (neither the QUIT_CHAR name),
# return up till MAX_NAMES names max.

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    count = 0
    for name in names:
        if name[0] == IGNORE_CHAR or not name.isalpha():
            continue
        if name[0] == QUIT_CHAR or count == MAX_NAMES:
            break
        count += 1
        yield name

