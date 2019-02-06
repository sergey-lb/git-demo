def calculate_trip_cost(distance_in_km):
    """
    >>> calculate_trip_cost(0)
    100.0

    >>> calculate_trip_cost(1)
    120.0

    :param distance_in_km:
    :return:
    """

    seat_cost = 100
    one_km_cost = 100 / 5

    total_cost = seat_cost + one_km_cost * distance_in_km
    return total_cost

# print(calculate_trip_cost(0))
