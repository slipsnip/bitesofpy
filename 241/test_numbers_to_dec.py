import pytest
from typing import List, Generator
from random import randint, choices

from numbers_to_dec import list_to_decimal

@pytest.fixture
def ints_to_dec():
    def _ints_to_dec(nums: List[int]) -> int:
        for num in nums:
            if not isinstance(num, int):
                raise TypeError
            elif num not in range(0, 9):
                raise ValueError
        decimal = 0
        for place, value in enumerate(nums[::-1]):
            decimal += 10**place * value
        return decimal
    return _ints_to_dec

@pytest.fixture
def get_random_ints():
    def _random_ints(count: int, *, inrange: bool=True) -> List[List[int]]:
        if inrange:
            options = list(range(0,9))  
        else:
            positive = range(10, 100)
            negative = range(-1, -100, -1)
            options = list(positive) + list(negative)
        
        gen_ints_ = lambda n, options: choices(options, k=n)
        return [gen_ints_(size, options) for size in range(1, count + 1)]
        
    return _random_ints

@pytest.mark.parametrize("not_ints", [['0', 4, 9], ['two', 3, 'eight'], [4.2, 5, 2]])
def test_list_to_decimal(get_random_ints, ints_to_dec, not_ints):

    in_range = get_random_ints(4) 
    out_of_range = get_random_ints(4, inrange=False)

    # TEST SELF DEFINED ints_to_dec works
    assert ints_to_dec([1,4,5,3]) == 1453
    assert ints_to_dec([0, 3]) == 3
    with pytest.raises(ValueError):
        ints_to_dec([-2])
    with pytest.raises(ValueError):
        ints_to_dec([0,12,6])
    with pytest.raises(TypeError):
        ints_to_dec(['4', '2']) 
    with pytest.raises(TypeError):
        ints_to_dec([2.34,6,3])

    # ACTUAL PYTESTS, AGAINST numbers_to_dec.py

    for valid_ints in in_range:
        assert list_to_decimal(valid_ints) == ints_to_dec(valid_ints)
    with pytest.raises(TypeError):
        list_to_decimal(not_ints)     
    for invalid_ints in out_of_range:
        with pytest.raises(ValueError):
            list_to_decimal(invalid_ints)




