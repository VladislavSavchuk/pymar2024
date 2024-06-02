"""Find specific character.
This program finds the character “#”.
If this character is found - removes the previous character from the string.
"""


def find_specific_character(data: str) -> str:
    """ This function finds the '#' character in a string
    and deletes the previous character if found.

    Args:
        data (str): The input string to be processed.

    Returns:
        str: The processed string with characters removed as specified.
    """

    result = []

    for char in data:
        if char != '#':
            result.append(char)
        elif result:
            result.pop()

    return ''.join(result)


assert find_specific_character("a#bc#d") == "bd", \
    "result should be 'bd'"
assert find_specific_character("abc#d##c") == "ac", \
    "result should be 'ac'"
assert find_specific_character("abc##d######") == "", \
    "function must return empty string"
assert find_specific_character("#######") == "", \
    "function must return empty string"
assert find_specific_character("") == "", \
    "function must return empty string"
