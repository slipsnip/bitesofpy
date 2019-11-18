import pytest
from fizzbuzz import fizzbuzz

# write one or more test functions below, they need to start with test_
@pytest.mark.parametrize(
    "number, ret",
    [
        (3, "Fizz"),
        (5, "Buzz"),
        (3, "Fizz"),
        (15, "Fizz Buzz"),
        (17, 17),
        (5 * 8, "Buzz"),
        (3 * 11, "Fizz"),
    ],
)
def test_fizzbuzz_return(number, ret):
    result = fizzbuzz(number)
    assert result == ret
