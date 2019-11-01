def countdown():
    """Write a generator that counts from 100 to 1"""
    for count in range(100, 0, -1):
        if count > 0:
            yield count
        else:
            raise StopIteration