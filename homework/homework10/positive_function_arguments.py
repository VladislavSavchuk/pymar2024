"""Positive functions arguments.
This program checks that all function arguments are positive numbers.
"""


def validate_arguments(func):
    """
    A decorator to validate that all arguments passed to a function
    are positive integers.

    This decorator iterates over the arguments passed to the decorated
    function and checks if each argument is a positive integer.
    If any argument is not a positive integer, it raises a ValueError
    with an appropriate message.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function with argument validation.

    Raises:
        ValueError: If any argument is not a positive integer.
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
    """
    Prints each argument passed to it.

    This function simply iterates over its arguments and prints each one.
    The arguments are validated to be positive integers
    by the validate_arguments decorator.

    Args:
        *args: Variable length argument list of integers.
    """
    for i in args:
        print(i)


simple_function(1, 2, 3, 4, 5)
simple_function(5, -4, 3, 2, 1)
