"""Module Sequence.
This program determines if a strict sequence can be obtained
by removing no more than one element from an array
"""


def is_strictly_increasing(sequence):
    """This function checks
    if the array is a strictly increasing sequence."""

    for i in range(len(sequence) - 1):
        # Проверяем, если текущий элемент больше следующего
        if sequence[i] >= sequence[i + 1]:
            return False
    return True


def become_strictly_increasing(sequence):
    """This function checks if a strictly increasing sequence
     can be obtained by removing at most one element."""

    for i in range(len(sequence) - 1):
        # Проверяем, если текущий элемент больше следующего
        if sequence[i] >= sequence[i + 1]:

            # Создаем копию массива
            sequence_without_current_elem = sequence.copy()

            # Удаляем текущий элемент из списка
            sequence_without_current_elem.pop(i)

            # Проверяем, является ли массив строго возрастающим
            # после удаления текущего элемента
            if is_strictly_increasing(sequence_without_current_elem):
                return True

            # Создаем копию массива
            sequence_without_next_elem = sequence.copy()

            # Удаляем следующий элемент из списка
            sequence_without_next_elem.pop(i + 1)

            # Проверяем, является ли массив строго возрастающим
            # после удаления следующего элемента
            if is_strictly_increasing(sequence_without_next_elem):
                return True

            # Если ни один из вариантов не приводит
            # к возрастающей последовательности, возвращаем False
            return False

    # Если весь массив уже строго возрастающий, возвращаем True
    return True


print(become_strictly_increasing([1, 2, 3]))
print(become_strictly_increasing([1, 2, 1, 2]))
print(become_strictly_increasing([1, 3, 2, 1]))
print(become_strictly_increasing([1, 2, 3, 4, 5, 3, 5, 6]))
print(become_strictly_increasing([40, 50, 60, 10, 20, 30]))
