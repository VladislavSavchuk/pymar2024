"""Module Statues.
This program identifies the amount of missing statues.
"""


def statues(list_digit):
    """This function identifies the amount of missing numbers in list"""
    # Сортируем список min -> max
    list_digit = sorted(list_digit)

    # Счетчик пропущенных чисел
    error_count = 0

    # Новый список для хранения всех чисел
    complete_list = []

    # for i in range(len(list_digit)):
    for i, _ in enumerate(list_digit):
        # Проверяем разность между текущим и предыдущим элементами
        # Если разность больше 1, значит, есть пропущенные числа
        while list_digit[i] - list_digit[i - 1] > 1:

            # Увеличиваем предыдущий элемент на 1
            list_digit[i - 1] += 1

            # Добавляем его в новый список
            complete_list.append(list_digit[i - 1])

            # Увеличиваем счетчик пропущенных чисел
            error_count += 1

        # Добавляем текущий элемент в новый список
        complete_list.append(list_digit[i])

    print(f"Количество пропущенных чисел: {error_count}")
    print(f"Обновленный список: {complete_list}")


statues([6, 2, 3, 8])
