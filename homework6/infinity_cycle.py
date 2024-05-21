""" Infinity cycle.
This program identifies, leads the code to an infinite cycle.
"""


def is_infinity_cycle(a, b):
    """This function identifies an infinite cycle."""
    while True:
        a += 1
        b -= 1
        if a == b:
            # Возвращаем False, если цикл не бесконечен
            return False
        # Добавляем условие для проверки, что цикл стал бесконечным
        if a > b:
            break   # Если a стало больше b, прерываем цикл
    # Возвращаем True, если цикл бесконечен
    return True


print("Для a = 2 и b = 6, результат:", is_infinity_cycle(2, 6))
print("Для a = 2 и b = 3, результат:", is_infinity_cycle(2, 3))
