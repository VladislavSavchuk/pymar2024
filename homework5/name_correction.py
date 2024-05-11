"""Name correction.
This program corrects the string starting with an uppercase letter
"""


def name_correction():
    """This function corrects a string starting with an uppercase letter"""
    # создаем строку в разных регистрах
    capital = "pARiS"

    # проводим проверку, если в строке будут буквы и цифры, без других символов
    if capital.isalnum():
        # исправляем строку при помощи метода title()
        print(capital.title())
    else:
        print("В строке есть другие символы")


name_correction()
