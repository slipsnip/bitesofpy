def sum_numbers(numbers=None):
    if numbers and len(numbers) > 0:
        return sum(numbers)
    elif not numbers:
        return sum(range(1,101)) if numbers == None else 0