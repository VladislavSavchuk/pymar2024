"""Find specific character.
This program finds the character “#”.
If this character is found - removes the previous character from the string.
"""


def find_specific_character(data: str) -> str:
    """
    This function finds the “#” character and
    if this character is found - deletes the previous character
    from the string

    data: str
    return: str
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

print("All tests passed!")
