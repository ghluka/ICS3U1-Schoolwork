def school_year(year:int) -> str:
    '''Returns a string stating based off what school year a person is in, if they are in elementary school, middle school or secondary school. Returns "unknown" if they are in a grade below 0 or above 12.'''
    if year < 0 or year > 12:
        return "unknown"
    if year >= 9:
        return f"secondary"
    elif year >= 6:
        return "middle"
    return "elementary"