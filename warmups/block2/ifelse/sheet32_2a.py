def school_year(year:int) -> str:
    '''Returns a string stating based off what school year a person is in, if they are in elementary school, middle school or secondary school.'''
    if year >= 9:
        return "secondary"
    elif year >= 6:
        return "middle"
    return "elementary"