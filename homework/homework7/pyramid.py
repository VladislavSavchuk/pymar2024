"""Module pyramid.
The program print pyramid from stars
"""


def pyramid_of_stars_1(base_size):
    """This function print pyramid from stars"""
    # print("Эта программа выводит комбинацию из звездочек в виде пирамиды")

    for r in range(base_size):
        # Вывод пробелов перед звездочками
        for _ in range(base_size - r - 1):
            print(' ', end='')
        # Вывод звездочек
        for _ in range(2 * r + 1):
            print('*', end='')
        # Переходим на новую строку
        print()


def pyramid_of_stars_2(base_size):
    """This function prints a pyramid of stars."""
    # print("Эта программа выводит комбинацию из звездочек в виде пирамиды")

    for r in range(base_size):
        # Вывод пробелов перед звездочками
        print(' ' * (base_size - r - 1), end='')
        # Вывод звездочек с пробелами между ними
        print('*' * (2 * r + 1))


# Вызываем функции и передаем значение
pyramid_of_stars_1(10)
pyramid_of_stars_2(10)
