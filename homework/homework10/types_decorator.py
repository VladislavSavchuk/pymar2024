"""Types decorator.
This program checks the type of function parameters,
converts them if necessary and then adds them up
"""

from functools import wraps


def typed(types):
    """Get type of parameter from function"""
    def decorator(func):
        """A decorator checks the type of function parameters
        and converts them"""
        @wraps(func)
        def wrapper(*args):
            list_arg = []
            for i in args:
                types(i)
                list_arg.append(types(i))
            return func(*list_arg)
        return wrapper
    return decorator


@typed(types=str)
def add_1(a: str, b: str) -> str:
    """This function returns the sum of all arguments"""
    return a + b


assert add_1("3", 5) == "35"
assert add_1(5, 5) == "55"
assert add_1('a', 'b') == 'ab'


@typed(types=int)
def add_2(a: int, b: int, c: int) -> int:
    """This function returns the sum of all arguments"""
    return a + b + c


assert add_2(5, 6, 7) == 18


@typed(types=float)
def add_3(a: float, b: float, c: float) -> float:
    """This function returns the sum of all arguments"""
    return a + b + c


assert add_3(0.1, 0.2, 0.4) == 0.7000000000000001
