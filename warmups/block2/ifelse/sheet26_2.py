def which_is_bigger(x:int, y:int) -> str:
    '''Returns a string stating which variable out of the two parameters are the biggest'''
    if x > y:
        return "first"
    elif x < y:
        return "second"
    return "equal"