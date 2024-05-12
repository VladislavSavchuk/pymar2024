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


def replace_and_del_value2():
    """This function added and deleted value in list"""
    # Список значений
    simple_list = [1, 0.5, "Hi", -100, 5, 6, 0, 100, "Vlad", True]
    print(f"Старый список: {simple_list}")

    # Добавляем значение 999 в список и удаляем элемент под индексом 6
    # переменная value заменена на знак подчеркивания "_"
    for index, _ in enumerate(simple_list):
        if index == 2:
            simple_list.insert(2, 999)
        elif index == 6:
            del simple_list[index]
            break  # Прерываем цикл после удаления элемента

    print(f"Новый список: {simple_list}")
    print()


replace_and_del_value2()
