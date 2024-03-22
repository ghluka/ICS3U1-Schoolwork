def is_quandrant1(x:float) -> bool:
    '''Returns a boolean value of whether or not an x-coordinate of a quadratic (-0.3x^2 + 5x + 20) is on the first quadrant of a cartesian plane'''
    y = -.3 * x ** 2 + 5 * x + 20
    return x > 0 and y > 0