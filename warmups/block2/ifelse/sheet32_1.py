def in_order(x:int, y:int, z:int) -> bool:
    '''Returns a boolean value of whether or not the 3 parameters are sorted'''
    return sorted([x, y, z]) == [x, y, z] or sorted([x, y, z], reverse=True) == [x, y, z]