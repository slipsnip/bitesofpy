from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapper(*args):
        if False in map(lambda arg: isinstance(arg, int), args):
            raise TypeError
        elif False in map(lambda arg: arg >= 0, args):
            raise ValueError
        else:
            return func(*args)
    return wrapper
