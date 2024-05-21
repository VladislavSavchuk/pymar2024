"""Add and delete value in list.
The program add and delete value in list
"""


def replace_and_del_value1():
    """This function added and deleted value in list"""
    # Список значений
    simple_list = [1, 0.5, "Hi", -100, 5, 6, 0, 100, "Vlad", True]
    print(f"Старый список: {simple_list}")

    # Добавляем элемент на 3 позицию в списке
    simple_list.insert(2, 999)

    # Удаляем элемент под индексом 6 в списке
    del simple_list[6]

    # Выводим результат
    print(f"Новый список: {simple_list}")
    print()


replace_and_del_value1()


def replace_and_del_value2(del_index):
    """This function added and deleted value in list"""
    # Список значений
    simple_list = [1, 0.5, "Hi", -100, 5, 6, 0, 100, "Vlad", True]
    print(f"Старый список: {simple_list}")

    # Проходим по списку
    # переменная value заменена на знак подчеркивания "_"
    for index, _ in enumerate(simple_list):
        if index == 2:
            # Добавляем значение 999 на 3 позицию в список
            simple_list.insert(2, 999)
            # Удаляем элемент под индексом переданным в функцию (6)
            del simple_list[del_index]
            break   # Прерываем цикл после удаления элемента

    print(f"Новый список: {simple_list}")


replace_and_del_value2(6)
