from itertools import compress


def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    uncommon = list(set(my_cities) ^ set(other_cities))
    return len(uncommon)
