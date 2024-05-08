"""Swap the words.
The program swap the words “Ivanou Ivan”
"""


def swap_words_1():
    """This function swaps words in a string using indexation"""
    # Задаем строку, которую хотим изменить
    name = "Ivanou Ivan"

    # Разбиваем строку на отдельные слова при помощи метода split()
    words = name.split()

    # Объединяем слова по индексу при помощи конкатенации
    swap_string = words[1] + ' ' + words[0]

    # Выводим результат
    print(f"Результат: {swap_string}")
    print()


def swap_words_2():
    """This function swaps words in a string using the reverse() method"""
    # Задаем строку, которую хотим изменить
    string = "Ivanou Ivan"

    # Разбиваем строку на отдельные слова при помощи метода split()
    words = string.split()

    # переворачиваем список слов при помощи метода reverse()
    words.reverse()

    # Объединяем слова обратно в строку с помощью функции join() через пробел.
    swap_words = ' '.join(words)

    # Выводим результат
    print(f"Результат: {swap_words}")
    print()


def swap_words_3():
    """This function swaps words in a string using the slice method"""
    # Задаем строку, которую хотим изменить
    name = "Ivanou Ivan"

    # Разбиваем строку на слова при помощи метода split() через пробел
    # изменяем порядок слов с помощью среза списка ([::-1])
    # объединяем слова в строку, разделяя их пробелом
    result = ' '.join(name.split(' ')[::-1])

    # Выводим результат
    print(f"Результат: {result}")
    print()


swap_words_1()
swap_words_2()
swap_words_3()
