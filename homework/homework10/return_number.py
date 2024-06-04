"""Return the number.
This program checks if the result of the function is a number
and prints an error message if it is not.
"""


def is_number(func):
    """
    A decorator that checks if the arguments and result
    of the function are numbers.

    This decorator calls the decorated function with its arguments,
    checks if the arguments and result are instances of int or float,
    and prints an error message if they are not.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function with argument
        and result type validation.
    """
    def wrapper(arg1, arg2):
        if (not isinstance(arg1, (int, float))
                or not isinstance(arg2, (int, float))):
            return None
        result = func(arg1, arg2)
        if not isinstance(result, (int, float)):
            print('Error! The result is not a number.')
        return result
    return wrapper


@is_number
def summ(a: int, b: int) -> int:
    """
    Returns the sum of two integers.

    This function takes two integers, adds them together,
    and returns the result.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    return a + b


assert summ(2, 2) == 4
assert summ(2, 'a'), 'Both arguments must be numbers'
assert summ(True, 'a'), 'Both arguments must be numbers'
