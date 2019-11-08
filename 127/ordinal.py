def get_ordinal_suffix(number):
    """Receives a number int and returns it appended with its ordinal suffix,
       so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.

       Rules:
       https://en.wikipedia.org/wiki/Ordinal_indicator#English
       - st is used with numbers ending in 1 (e.g. 1st, pronounced first)
       - nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second)
       - rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
       - As an exception to the above rules, all the "teen" numbers ending with
         11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th,
         pronounced one hundred [and] twelfth)
       - th is used for all other numbers (e.g. 9th, pronounced ninth).
       """
    # last two digits of number as str unless less than ten 
    number_str = str(number)
    trans = {'11': 'th', '12': 'th', '13': 'th', '1': 'st', '2': 'nd', '3': 'rd'}
    ending = number_str[-2:] if number > 10 and number_str[-2:] in trans else str(number)[-1]
    suffix = trans[ending] if ending in trans else 'th'
    return str(number) + suffix


