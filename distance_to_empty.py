def calculate_distance_to_empty(consumption_per_100_km, fuel_level):
    """
    >>> calculate_distance_to_empty(10, 10)
    100.0

    >>> calculate_distance_to_empty(10, 5)
    50.0

    :param consumption_per_100_km:
    :param fuel_level:
    :return:
    """

    consumption_per_km = consumption_per_100_km/100
    distance_to_empty = fuel_level/consumption_per_km
    return distance_to_empty

consumption_per_100_km = float(input('Введите расход топлива на 100 км ') )
fuel_level = float(input('Введите объем имеющегося топлива ') )

distance_to_empty = calculate_distance_to_empty(consumption_per_100_km, fuel_level)
distance_to_empty = int(distance_to_empty // 1)

print('Топлива хватит примерно на ' + str(distance_to_empty) + ' км')