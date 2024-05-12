"""Convert list to string.
The program convert list to string
"""


def convert_list_to_string():
    """This function convert list to string uses join() method"""
    # Список
    list_1 = ["I", "love", "arrays", "they", "are", "my", "favorite"]

    # Конвертируем список в строку при помощи метода join()
    list_to_array = ' '.join(list_1)

    # Выводим результат
    print(f"Новый строка из списка значений: {list_to_array}")


convert_list_to_string()
