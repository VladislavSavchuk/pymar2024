"""Convert string to list.
The program convert string to list
"""


def convert_string_to_list():
    """This function convert string to list split() method"""
    # Создаем строку
    full_name = "Robin Singh"

    # Конвертируем строку в список при помощи метода split()
    convert_to_list = full_name.split()

    # Выводим результат
    print(f"Новый список: {convert_to_list}")


convert_string_to_list()
