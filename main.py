import lib

room_length = float(input('Введите длину комнаты в метрах: '))
room_width = float(input('Введите ширину комнаты в метрах: '))
room_height = float(input('Введите высоту комнаты в метрах: '))

roll_width = float(input('Введите ширину рулона в см: '))
roll_width = roll_width / 100
roll_length = float(input('Введите длину рулона в метрах: '))

pattern_shift = float(input('Введите величину смещения для стыковки в см: '))
pattern_shift = pattern_shift / 100

height_reserve = 0.1
room_height = room_height + height_reserve

perimeter = lib.calculate_perimeter(room_width, room_length)

odd_strips_required = lib.calculate_odd_strips_required(perimeter, roll_width)
even_strips_required = lib.calculate_even_strips_required(perimeter, roll_width)

rolls_for_odd = lib.calculate_rolls_for_odd_strips(odd_strips_required, roll_length, pattern_shift, room_height)
rolls_for_even = lib.calculate_rolls_for_even_strips(even_strips_required, roll_length, room_height)

rolls_required = rolls_for_odd + rolls_for_even

print('Вам потребуется ' + str(rolls_required) + ' рулонов')
