"""Remove spaces.
The program that removes a space at the beginning, at the end of a line
"""


def remove_spaces():
    """This function removes a space at the beginning, at the end of a line"""
    # Задаем строку с пробелами в начале и в конце, которую хотим изменить
    name = " onetesttwo three "

    # Удаляем пробелы в начале строки при помощи метода lstrip()
    print(f"Удален пробел в начале строки:{name.lstrip()}")

    # Удаляем пробелы в конце строки при помощи метода rstrip()
    print(f"Удален пробел в конце строки:{name.rstrip(' ')}")
    print()


remove_spaces()


def remove_whitespace(my_string):
    """This function removes leading and trailing whitespace from a string."""
    return my_string.strip()


# Задаем строку с пробелами в начале и в конце, которую хотим изменить
GREETING = "   Hello, world!   "

# присваиваем функцию переменной
RESULT = remove_whitespace(GREETING)

# выводим результат
print(f"Строка без пробелов в начале и конце:{RESULT}")
