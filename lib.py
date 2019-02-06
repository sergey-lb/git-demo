

# common functions


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


def calculate_perimeter(width, length):
    """

    >>> calculate_perimeter(4, 6)
    20
    """

    result = (width + length) * 2
    return result


# distance_to_empty.py functions


def calculate_distance_to_empty(consumption_per_100_km, fuel_level):
    """

    >>> calculate_distance_to_empty(10, 10)
    100.0

    >>> calculate_distance_to_empty(10, 5)
    50.0
    """

    consumption_per_km = consumption_per_100_km/100
    distance_to_empty = fuel_level/consumption_per_km
    return distance_to_empty


# rolls_required.py functions


def calculate_number_of_strips(perimeter, roll_width):
    """

    >>> calculate_number_of_strips(18, 1.06)
    17
    """

    result = round_up(perimeter / roll_width)
    return result


def calculate_odd_strips_required(perimeter, roll_width):
    """

    >>> calculate_odd_strips_required(18, 1.06)
    9
    """

    number_of_strips = round_up(perimeter / roll_width)
    result = round_up(number_of_strips / 2)
    return result


def calculate_even_strips_required(perimeter, roll_width):
    """

    >>> calculate_even_strips_required(18, 1.06)
    8
    """

    number_of_strips = round_up(perimeter / roll_width)
    result = round_down(number_of_strips / 2)
    return result


def calculate_rolls_for_odd_strips(number_of_strips, roll_length, pattern_shift, room_height):
    """

    >>> calculate_rolls_for_odd_strips(9, 10, 0.32, 2.7)
    3
    """

    odd_strips_in_roll = round_down((roll_length - pattern_shift) / room_height)
    result = round_up(number_of_strips / odd_strips_in_roll)
    return result


def calculate_rolls_for_even_strips(number_of_strips, roll_length, room_height):
    """

    >>> calculate_rolls_for_even_strips(8, 10, 2.7)
    3
    """

    even_strips_in_roll = round_down(roll_length / room_height)
    result = round_up(number_of_strips / even_strips_in_roll)
    return result
