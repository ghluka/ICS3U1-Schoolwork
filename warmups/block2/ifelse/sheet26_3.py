import math

def largest_circle_area(width:float, height:float) -> str:
    '''Returns the area of the largest possible circle that can be fit in a rectangle'''
    if width > height:
        radius = height / 2
    else:
        radius = width / 2
    return math.pi * radius ** 2