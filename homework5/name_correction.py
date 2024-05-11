"""Name correction.
This program corrects the string starting with an uppercase letter
"""


def name_correction():
    """This function corrects a string starting with an uppercase letter"""
    # создаем строку в разных регистрах
    capital = "pARiS"
    # исправляем строку при помощи метода title()
    print(capital.title())


name_correction()
