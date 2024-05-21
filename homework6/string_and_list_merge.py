"""String and list merge.
The program string and list merge
"""


def string_and_list_merge1():
    """This function string and list merge"""
    # Список имён
    full_name = ['Ivan', 'Ivanou']

    # Строки с городом и страной
    city = 'Minsk'
    country = 'Belarus'

    # Конвертируем список в строку при помощи метода join()
    convert_to_array = " ".join(full_name)

    # Выводим результат
    print(f'“Привет, {convert_to_array}! Добро пожаловать в {city} {country}"')
    print()


string_and_list_merge1()


def string_and_list_merge2():
    """This function string and list merge through indexation"""
    # Список имён
    names = ["Ivan", "Ivanou"]

    # Строки с городом и страной
    city = "Minsk"
    country = "Belarus"

    # Создание строки с использованием форматирования строк
    greeting = (f'"Привет, {names[0]} {names[1]}! '
                f'Добро пожаловать в {city} {country}"')

    # Выводим результат
    print(greeting)


if __name__ == "__main__":
    string_and_list_merge2()
