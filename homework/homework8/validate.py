"""Module Validate.
This program checks credit card"""


def validate_card(number_card):
    """This function checks credit card."""

    # Проверка ввода данных
    check_number_card = check_number_credit_card(number_card)

    # Проверка существования карты
    is_valid = is_credit_card_exist(check_number_card)
    return is_valid


def check_number_credit_card(number_card):
    """This function checks number credit card."""

    while True:
        # Проверяем введенный номер карты
        if 11 <= len(number_card) <= 16 and number_card.isdigit():
            return number_card
        number_card = input('Error! Check data.'
                            'Enter card number 11-16 digits: ')


def is_credit_card_exist(check_number_card):
    """This function checks credit card algorithm of Luna."""

    # Преобразуем каждый элемент строки в тип 'int' и упаковываем в список
    digits = list(map(int, check_number_card[:]))

    # Проведем итерацию в обратном порядке через одну позицию
    for i in range(len(digits) - 2, -1, -2):
        # Необходимо умножить каждую вторую цифру с конца на 2
        digits[i] *= 2
        # Если удвоенная цифра больше 9, то отнимаем от неё 9.
        if digits[i] > 9:
            digits[i] -= 9

    # Суммируем все цифры
    total_sum = sum(digits)

    # Проверяем, что сумма кратна 10
    return total_sum % 10 == 0


assert validate_card('378282246310005'), 'must be True'
assert validate_card('5610591081018250'), 'must be True'
assert validate_card('30569309025904'), 'must be True'
assert not validate_card('76009244561'), 'must be False'
