from builtins import round


def round_down(number):
    """

    >>> round_down(2.3)
    2
    """

    number = number // 1
    number = int(number)
    return number


def round_up(number):
    """

    >>> round_up(2.3)
    3
    """

    number = number // 1 + (number % 1 > 0)
    number = int(number)
    return number


def calculate_rolls_required(room_length, room_width, room_height, roll_width, roll_length, pattern_shift):
    """

    >>> calculate_rolls_required(4.5, 3.5, 2.7, 1.06, 10, 0.32)
    6
    """

    perimeter = (room_length + room_width) * 2

    number_of_strips = round_up(perimeter / roll_width)

    odd_strips_required = round_up(number_of_strips / 2)
    even_strips_required = round_down(number_of_strips / 2)

    odd_strips_in_roll = round_down((roll_length - pattern_shift) / room_height)
    rolls_for_odd = round_up(odd_strips_required / odd_strips_in_roll)

    even_strips_in_roll = round_down(roll_length / room_height)
    rolls_for_even = round_up(even_strips_required / even_strips_in_roll)

    rolls_required = rolls_for_odd + rolls_for_even

    return rolls_required


def validate_params(args):
    """
    >>> validate_params({})
    ['Длина помещения обязательное поле', 'Ширина помещения обязательное поле', 'Высота помещения обязательное поле', 'Ширина рулона обязательное поле', 'Длина рулона обязательное поле']

    >>> validate_params({
    ...     'room_length': '',
    ...     'room_width': '',
    ...     'room_height': '',
    ...     'roll_width': '',
    ...     'roll_length': '',
    ...     'pattern_shift': ''
    ... })
    ['Длина помещения обязательное поле', 'Ширина помещения обязательное поле', 'Высота помещения обязательное поле', 'Ширина рулона обязательное поле', 'Длина рулона обязательное поле']

    >>> validate_params({
    ...     'room_length': '10,1',
    ...     'room_width': '10.1',
    ...     'room_height': ' 10.1',
    ...     'roll_width': '10',
    ...     'roll_length': '10',
    ...     'pattern_shift': '10'
    ... })
    []

    >>> validate_params({
    ...     'room_length': '10,1.1',
    ...     'room_width': '10,1',
    ...     'room_height': '10.1',
    ...     'roll_width': '10',
    ...     'roll_length': '10',
    ...     'pattern_shift': '10'
    ... })
    ['Длина помещения должно быть числом']
    """

    errors = []

    fields = {
        'room_length': {
            'label': 'Длина помещения',
            'is_required': True
        },
        'room_width': {
            'label': 'Ширина помещения',
            'is_required': True
        },
        'room_height': {
            'label': 'Высота помещения',
            'is_required': True
        },
        'roll_width': {
            'label': 'Ширина рулона',
            'is_required': True
        },
        'roll_length': {
            'label': 'Длина рулона',
            'is_required': True
        },
        'pattern_shift': {
            'label': 'Смещение для стыковки',
            'is_required': False
        }
    }

    for key, field in fields.items():
        val = args.get(key)
        if val is None:
            val = ''

        val = val.strip()

        if not val and field['is_required']:
            error = f"{field['label']} обязательное поле"
            errors.append(error)

        if not val:
            continue

        val = val.replace(',', '.')
        if not val.replace('.', '', 1).isdigit():
            error = f"{field['label']} должно быть числом"
            errors.append(error)

    return errors


def format_params(args):
    """
    >>> format_params({
    ...     'room_length': '10,1',
    ...     'room_width': '10.1',
    ...     'room_height': ' 10.1',
    ...     'roll_width': '10',
    ...     'roll_length': '10',
    ...     'pattern_shift': '10'
    ... })
    {'room_length': 10.1, 'room_width': 10.1, 'room_height': 10.2, 'roll_width': 0.1, 'roll_length': 10.0, 'pattern_shift': 0.1}

    >>> format_params({
    ...     'room_length': '10',
    ...     'room_width': '10,1',
    ...     'room_height': '10.1',
    ...     'roll_width': '10',
    ...     'roll_length': '10',
    ...     'pattern_shift': ''
    ... })
    {'room_length': 10.0, 'room_width': 10.1, 'room_height': 10.2, 'roll_width': 0.1, 'roll_length': 10.0, 'pattern_shift': 0.0}

    >>> format_params({})
    {'room_length': 0, 'room_width': 0, 'room_height': 0.1, 'roll_width': 0.0, 'roll_length': 0, 'pattern_shift': 0.0}
    """

    params = {
        'room_length': 0,
        'room_width': 0,
        'room_height': 0,
        'roll_width': 0,
        'roll_length': 0,
        'pattern_shift': 0
    }

    for key in params.keys():
        val = args.get(key)
        if not val:
            continue

        val = val.strip().replace(',', '.')
        params[key] = float(val)

    params['roll_width'] = params['roll_width'] / 100
    params['pattern_shift'] = params['pattern_shift'] / 100

    height_reserve = 0.1
    params['room_height'] = params['room_height'] + height_reserve

    return params


def validate_roll_length(roll_length, room_height, pattern_shift):
    """
    >>> validate_roll_length(10.42, 10.1, 0.32)
    []

    >>> validate_roll_length(10.41, 10.1, 0.32)
    ['Длина рулона должна быть минимум на 42 см больше высоты комнаты']
    """

    errors = []

    if room_height > roll_length - pattern_shift:
        height_reserve = 0.1
        min_roll_length = round((height_reserve + pattern_shift) * 100)
        error = 'Длина рулона должна быть минимум на ' + str(min_roll_length) + ' см больше высоты комнаты'
        errors.append(error)

    return errors
