"""Moto trip.
The program calculate time trip and Returns the answer as
the sum of digits that the digital timer will show in hh:mm format.
"""


def calculate_current_time():
    """This function calculated current time moto trip"""
    # время поездки (в минутах)
    time_trip = int(input('Enter time: '))

    # переменная для перевода времени поездки
    convert_hour = 60

    # перевод времени в часы и минуты
    current_hours = time_trip // convert_hour
    current_minutes = time_trip % convert_hour

    print(f'Время поездки {current_hours} часа(-ов)'
          f' {current_minutes} минут(-а)')

    # Преобразуем часы и минуты в строки и дополним нулями, если необходимо
    hours_str = str(current_hours).zfill(2)
    minutes_str = str(current_minutes).zfill(2)

    # накопитель
    digit_sum = 0

    # Суммируем цифры часов и минут
    for digit in hours_str + minutes_str:
        digit_sum += int(digit)

    print("Сумма цифр времени:", digit_sum)


calculate_current_time()
