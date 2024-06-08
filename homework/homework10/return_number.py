"""Return the number.
This program checks if the result of the function is a number
and prints an error message if it is not.
"""


def is_number(func):
    """ A decorator that checks if the result of the function is a number"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            print('Error! The result is not a number.')
        return result
    return wrapper


@is_number
def summ(*args, **kwargs):
    """Returns the sum of all arguments if is number"""
    return sum(args) + sum(kwargs.values())


assert summ(2, 2) == 4, 'result must be = 4'
assert summ(2, b=4) == 6, 'result must be = 6'
assert summ(1.5, 2.5) == 4.0, 'result must be = 4.0'
assert summ(a=2, b=3.5) == 5.5, 'result must be = 5.5'
