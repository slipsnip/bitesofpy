def sum_numbers(numbers=None):
    if numbers == None:
        numbers = [x + 1 for x in range(100)]
    sum = 0
    for x in numbers:
        sum += x
    return sum