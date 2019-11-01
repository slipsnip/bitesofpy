def countdown():
    """Write a generator that counts from 100 to 1"""
    for count in range(100, 0, -1):
        yield count