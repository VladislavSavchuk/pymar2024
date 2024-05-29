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


assert find_specific_character("a#bc#d") == "bd"
assert find_specific_character("abc#d##c") == "ac"
assert find_specific_character("abc##d######") == ""
assert find_specific_character("#######") == ""
assert find_specific_character("") == ""

print("All tests passed!")
