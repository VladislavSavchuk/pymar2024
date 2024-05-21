"""Convert string to list.
The program convert string to list
"""


def convert_string_to_list1():
    """This function convert string to list uses split() method"""
    # Создаем строку
    favorite_string = "I love arrays they are my favorite"

    # Разделитель
    sep = " "

    # Используем цикл 'for' для доб-ия разделителя к каждому элементу списка
    result = [value + sep for value in favorite_string.split(sep)]

    # Выводим результат
    print(f"Новый список: {result}")
    print()


convert_string_to_list1()


def convert_string_to_list2():
    """This function convert string to list uses split() method"""
    # Строка
    favorite_string = "I love arrays they are my favorite"

    # Разделитель
    sep = " "

    # Разбиваем строку на список с помощью метода split()
    values = favorite_string.split(sep)

    # Создаем пустой список для результата
    result = []

    # Цикл 'for' для добавления разделителя к каждому элементу списка
    for element in values:
        result.append(element + sep)

    # Выводим результат
    print(f"Новый список: {result}")


convert_string_to_list2()
