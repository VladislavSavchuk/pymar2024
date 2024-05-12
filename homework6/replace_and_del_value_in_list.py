"""Add and delete value in list.
The program replaced and delete value in list
"""


def replace_and_del_value1():
    """This function replaced and deleted value in list"""
    # Список значений
    simple_list = [1, 0.5, "Hi", -100, 5, 6, 0, 100, "Vlad", True]
    print(f"Старый список: {simple_list}")

    # Заменяем элемент на 3 позиции в списке
    simple_list[2] = 'Hello'

    # Удаляем элемент под индексом 6 в списке
    del simple_list[6]

    # Выводим результат
    print(f"Новый список: {simple_list}")
    print()


replace_and_del_value1()


def replace_and_del_value2():
    """This function replaces and deletes value in list"""
    # Список значений
    simple_list = [1, 0.5, "Hi", -100, 5, 6, 0, 100, "Vlad", True]
    print(f"Старый список: {simple_list}")

    # Заменяем "Hi" на "Hello" и удаляем 0
    for index, value in enumerate(simple_list):
        if value == "Hi":
            simple_list[index] = 'Hello'
        elif index == 6:
            del simple_list[index]
            break  # Прерываем цикл после удаления элемента

    print(f"Новый список: {simple_list}")
    print()


replace_and_del_value2()
