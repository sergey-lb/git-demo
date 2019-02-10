

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
