from string import ascii_letters, digits


"""Checks if given argument is an alphanumeric character
    i.e. a member of one of ascii_letters or digits
    typecasts to str
    returns False on empty string
    """


def is_alphanumeric(test):
    str_test = str(test).lower()
    return len(str_test) == 1 and str_test in ascii_letters + digits


def get_index_different_char(chars):
    alphanum_filtered = {index: char for index, char in enumerate(chars) if is_alphanumeric(char)}
    if len(alphanum_filtered) == 1:
        return list(alphanum_filtered)[0]
    else:
        alphanum_filtered = {index: char for index, char in enumerate(chars) if not is_alphanumeric(char)}
        return list(alphanum_filtered)[0]
