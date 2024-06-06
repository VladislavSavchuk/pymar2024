"""Function cache.
This program caches the results of a function call and returns
the cached value on repeated calls with the same arguments
"""
from functools import wraps


def cache(func):
    """A decorator caches the results of a function call and returns
    the cached value on repeated calls with the same arguments.
    """
    caches = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create keys from tuple 'args' and a pair of tuple 'kwargs'
        key = (args, tuple(kwargs.items()))
        if key not in caches:
            caches[key] = func(*args, **kwargs)
        return caches[key]
    return wrapper


@cache
def fibonacci(n: int) -> int:
    """Function for calculating Fibonacci numbers"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(5) == 5, 'result must be = 5'
assert fibonacci(10) == 55, 'result must be = 55'
assert fibonacci(5) == 5, 'result must be = 5 and from caches'
