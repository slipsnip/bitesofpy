from itertools import permutations

def find_number_pairs(numbers, N=10):
    """ find pairs of numbers in numbers list that add up to N
        for each pair in permutations of 2 numbers that add up to N sort then
        retuple to correct for situations where two or more tuples are identicle
        not by order but by value of the pair"""
    pairs = {tuple(sorted(pair)) for pair in permutations(numbers, 2) if sum(pair) == N}
    return list(pairs)
