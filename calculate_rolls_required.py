def round_up(number):
    """
    >>> round_up(2.3)
    3

    :param number:
    :return:
    """

    number = number // 1 + (number % 1 > 0)
    number = int(number)
    return number


room_length = float(input('Введите длину комнаты в метрах: '))
room_width = float(input('Введите ширину комнаты в метрах: '))
room_height = float(input('Введите высоту комнаты в метрах: '))

height_reserve = 0.1

roll_width = float(input('Введите ширину рулона в см: '))
roll_width = roll_width / 100
roll_length = float(input('Введите длину рулона в метрах: '))

pattern_shift = float(input('Введите величину смещения для стыковки в см: '))
pattern_shift = pattern_shift / 100

room_height = room_height + height_reserve

perimeter = (room_width + room_length) * 2

number_of_strips = round_up(perimeter / roll_width)
number_of_odd_strips = round_up(number_of_strips / 2)
number_of_even_strips = (number_of_strips / 2) // 1

odd_strips_in_roll = ((roll_length - pattern_shift) / room_height) // 1
even_strips_in_roll = (roll_length / room_height) // 1

odd_rolls_required = round_up(number_of_odd_strips / odd_strips_in_roll)
even_rolls_required = round_up(number_of_even_strips / even_strips_in_roll)

rolls_required = int(odd_rolls_required + even_rolls_required)

print('Вам потребуется ' + str(rolls_required) + ' рулонов')