"""Module game 'Bulls and Cows'.
The program guesses a sequence of numbers.
"""
import random

# Количество цифр в загадываемом слове
COUNT = 4


# pylint: disable=invalid-name
def generate_random_number(count):
    """This function generates a random number with non-repeating digits."""
    # Создаем список цифр от 0 до 9
    digits = list(range(10))

    # Перемешиваем их при помощи модуля shuffle()
    random.shuffle(digits)

    # Преобразуем первых 4 числа в строку каждый и объединяем
    random_numbers = ''.join(map(str, digits[:count]))
    return random_numbers


def game(target_number):
    """This function guesses a sequence of numbers."""

    while True:
        user_numbers = input("Введите 4-значное число "
                             "с неповторяющимися цифрами: ")

        # Проверка на правильное количество цифр и уникальность
        if (len(user_numbers) != COUNT or len(set(user_numbers)) != COUNT
                or not user_numbers.isdigit()):
            print("Ошибка!")
            # Переход на новую итерацию цикла
            continue

        # Накопители
        cows = 0
        bulls = 0

        # Проходим перебором по каждому значению
        for i in range(COUNT):
            # Проверяем совпадения по позициям в тайном числе
            if user_numbers[i] == target_number[i]:
                bulls += 1
            elif user_numbers[i] in target_number:
                cows += 1

        # Проверяем всю последовательность
        if bulls == COUNT:
            print("Вы выиграли!!!")
            return

        print(f"Коровы: {cows}. Быки: {bulls}")


# Генерация случайного числа и запуск игры
random_number = generate_random_number(COUNT)
game(random_number)
