"""Positive functions arguments.
This program checks that all function arguments are positive numbers.
"""


def validate_arguments(func):
    """ A decorator to validate that all arguments passed to a function
    are positive integers. If any argument is not a positive integer
    show ValueError.
    """
    def wrapper(*args):
        for i in args:
            if not isinstance(i, int) or i <= 0:
                raise ValueError(f"Invalid argument: {i}."
                                 f"All arguments must be positive numbers.")
        func(*args)
    return wrapper


@validate_arguments
def simple_function(*args):
    """Prints each argument passed to it"""
    for i in args:
        print(i)


simple_function(1, 2, 3, 4, 5)
simple_function(5, -4, 3, 2, 1)
