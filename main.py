from lib import calculate_rolls_required

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

rolls_required = calculate_rolls_required(room_length, room_width, room_height, roll_width, roll_length, pattern_shift)

print('Вам потребуется ' + str(rolls_required) + ' рулонов')
