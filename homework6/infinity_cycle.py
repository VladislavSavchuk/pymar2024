""" Infinity cycle.
This program identifies, leads the code to an infinite cycle.
"""


def is_infinity_cycle(a, b):
    """This function identifies an infinite cycle."""
    while a != b:
        a += 1
        b -= 1
    return a != b


print(f"Этот цикл будет бесконечен. {is_infinity_cycle(2, 3)}")
print(f"Этот цикл НЕ бесконечен. {is_infinity_cycle(2, 6)}")
