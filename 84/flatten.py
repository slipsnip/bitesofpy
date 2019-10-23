def flatten(list_of_lists):
    flat_list = []
    for index, item in enumerate(list_of_lists):
        if isinstance(item, tuple) or isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)

    return flat_list
