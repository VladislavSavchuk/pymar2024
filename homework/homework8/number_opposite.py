"""Module the number opposite.
This program look for the number opposite number in circle"""


def main(n, first_number):
    """This general function prints the opposite number"""

    # Проверка валидности числа
    if not validate_number(n):
        return

    # Вызываем функцию нахождения числа напротив числа в окружности
    return find_opposite_number(n, first_number)


def validate_number(n):
    """This function checks if the number is even, positive and integer"""

    # Проверяем число
    if isinstance(n, int) and n % 2 == 0 and n > 0:
        return True
    print("'n' must be an integer, positive and even number.")
    return False


def find_opposite_number(n, first_number):
    """This function finds the opposite number in a circle"""

    # Находим половину окружности
    half_circle = n // 2

    # Добавляем это значение к first_number
    opposite_number = half_circle + first_number

    # Находим остаток от деления полученного значения на 'n'
    result = opposite_number % n
    return result


assert (main(10, 2)) == 7, 'opposite number must be = 7'
assert not main(25, 1), "n must be an integer, positive and even number."
assert not main(0, 8), "n must be an integer, positive and even number."
assert not main(-13, 3), "n must be an integer, positive and even number."
assert not main(5.2, 3), "n must be an integer, positive and even number."
