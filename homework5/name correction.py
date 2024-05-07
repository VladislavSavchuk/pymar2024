"""Name correction.
This program corrects the string starting with an uppercase letter
"""


def name_correction():
    """This function corrects a string starting with an uppercase letter followed by lowercase letters"""
    # создаем строку в разных регистрах
    capital = "pARiS"

    # проводим проверку, что строка состоит только из букв
    if capital.isalpha():
        # исправляем строку при помощи метода title()
        print(capital.title())
    else:
        print("В строке есть не только буквы")


name_correction()
