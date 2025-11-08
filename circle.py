import math

def area(r):
    '''
    Возвращает площадь круга.

    Параметры:
        r (float): радиус круга

    Возвращаемое значение:
        float: площадь круга
    '''
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга.

    Параметры:
        r (float): радиус круга

    Возвращаемое значение:
        float: периметр круга
    '''
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r
