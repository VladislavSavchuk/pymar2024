"""Count character.
This program calculate count character in the string.
"""

from itertools import groupby


def calculate_count_character(text: str) -> str:
    """This function uses 'group by' from the 'itertools' module to group
    consecutive identical elements in an iterator.
    It creates an iterator that returns the key and groups
    consecutive items, and then counts the number of those items.

    Args:
        text (str): The input string to be processed.

    Returns:
        str: The processed string with characters removed as specified.
    """

    result = []

    for char, group in groupby(text):
        count = len(list(group))
        if count > 1:
            result.append(char + str(count))
        else:
            result.append(char)

    return ''.join(result)


assert calculate_count_character("cccbba") == 'c3b2a', \
    "result should be 'c3b2a'"
assert calculate_count_character("abeehhhhhccced") == "abe2h5c3ed", \
    "result should be 'abe2h5c3ed'"
assert calculate_count_character("aaabbceedd") == "a3b2ce2d2", \
    "result should be 'a3b2ce2d2'"
assert calculate_count_character("abcde") == "abcde", \
    "result should be 'abcde'"
assert calculate_count_character("aaabbdefffff") == "a3b2def5", \
    "result should be 'a3b2def5'"
