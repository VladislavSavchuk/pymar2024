"""Replace the symbol.
The program changes the character "#" to character "/"
"""


def changes_character_1():
    """The 'replace()' method is used to replace a character in a string"""
    # Создаем строку
    my_string = 'www.my_site.com#about'

    # Заменяем символ "#" при помощи метода replace() и выводим результат
    print(my_string.replace("#", "/"))
    print()


def changes_character_2():
    """The function is used to replace a character in a string using the 'for' cycle and assignment operator."""
    # Создаем строку
    my_string = "www.my_site.com#about"

    # Создаем пустую строку
    new_str = ""
    # Проходим перебором по каждому символу в строке
    for ch in my_string:
        if ch == '#':
            # Заменяем символ "#" при помощи оператора присваивания
            new_str += "/"
        else:
            new_str += ch
    # Выводим результат
    print(new_str)
    print()


def changes_character_3():
    """The function is used to replace a character in a string used find() method"""
    # Создаем строку
    my_str = "www.my_site.com#about"

    # Находим индекс символа "#" при помощи метода find()
    symbol = my_str.find("#")

    # Заменяем найденный символ "#" при помощи метода replace()
    replace_symbol = my_str.replace(str(symbol), "/")

    # Выводим результат
    print(replace_symbol)


changes_character_1()
changes_character_2()
changes_character_3()
