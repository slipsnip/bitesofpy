from pudb import set_trace


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    deduped_names = []
    index = 0
    # for each name count how many times it appears in remainder of
    # NAMES list and if none, title case & store it
    for full_name in NAMES:
        if NAMES[index + 1:].count(full_name) == 0:
            # split name into list [first_name, last_name]
            split_name = full_name.split()
            # function that title cases a given name
            function_title_case = (lambda name: name[0].upper() + name[1:])
            # apply the title case
            cased_split_name = list(map(function_title_case, split_name))
            # glue it back together
            title_cased_name = ' '.join(list(cased_split_name))
            # save it
            deduped_names.append(title_cased_name)
        index += 1
    return deduped_names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    sorted_names = dedup_and_title_case_names(names)
    function_get_surname = (lambda full_name: full_name.split()[1])
    sorted_names.sort(key=function_get_surname, reverse=True)
    return sorted_names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    title_cased_names = dedup_and_title_case_names(names)
    # split full_name and return len of first_name
    function_firstname_length = (lambda full_name: len(full_name.split()[0]))
    """get smallest first_name via builtin min and
    function_firstname_length"""
    smallest_first = min(title_cased_names, key=function_firstname_length)
    smallest_first = smallest_first.split()[0]
    return smallest_first
