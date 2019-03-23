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


def collect_params_from_request_args(args):
    """
    >>> collect_params_from_request_args({
    ...    'room_length': '10',
    ...    'room_width': '10',
    ...    'room_height': '10',
    ...    'roll_width': '10',
    ...    'roll_length': '10',
    ...    'pattern_shift': ''
    ... })
    {'room_length': 10.0, 'room_width': 10.0, 'room_height': 10.1, 'roll_width': 0.1, 'roll_length': 10.0, 'pattern_shift': 0.0}

    >>> collect_params_from_request_args({
    ...    'room_length': '10',
    ...    'room_width': '10',
    ...    'room_height': '10',
    ...    'roll_width': '10',
    ...    'roll_length': '10',
    ...    'pattern_shift': '32'
    ... })
    {'room_length': 10.0, 'room_width': 10.0, 'room_height': 10.1, 'roll_width': 0.1, 'roll_length': 10.0, 'pattern_shift': 0.32}

    >>> collect_params_from_request_args({})
    False

    >>> collect_params_from_request_args({
    ...    'room_length': '',
    ...    'room_width': '',
    ...    'room_height': '',
    ...    'roll_width': '',
    ...    'roll_length': '',
    ...    'pattern_shift': ''
    ... })
    False

    >>> collect_params_from_request_args({
    ...    'room_length': '10',
    ...    'room_width': '',
    ...    'room_height': '',
    ...    'roll_width': '',
    ...    'roll_length': '',
    ...    'pattern_shift': ''
    ... })
    False
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
        if val:
            val = val.strip()
        if not val and key != 'pattern_shift':
            return False
        if val:
            params[key] = float(val)

    params['roll_width'] = params['roll_width'] / 100
    params['pattern_shift'] = params['pattern_shift'] / 100

    height_reserve = 0.1
    params['room_height'] = params['room_height'] + height_reserve

    return params


def validate_params(params):
    """
    >>> validate_params({
    ...     'room_length': 10.0,
    ...     'room_width': 10.0,
    ...     'room_height': 10.1,
    ...     'roll_width': 0.1,
    ...     'roll_length': 10.42,
    ...     'pattern_shift': 0.32
    ... }) is None
    True

    >>> validate_params(False)
    'Введите все обязательные (*) значения'

    >>> validate_params({
    ...     'room_length': 10.0,
    ...     'room_width': 10.0,
    ...     'room_height': 10.1,
    ...     'roll_width': 0.1,
    ...     'roll_length': 10.0,
    ...     'pattern_shift': 0.32
    ... })
    'Длина рулона должна быть минимум на 42 см больше высоты комнаты'
    """

    if not params:
        return 'Введите все обязательные (*) значения'

    if params['room_height'] > params['roll_length'] - params['pattern_shift']:
        height_reserve = 0.1
        min_roll_length = round((height_reserve + params['pattern_shift']) * 100)
        return 'Длина рулона должна быть минимум на ' + str(min_roll_length) + ' см больше высоты комнаты'
