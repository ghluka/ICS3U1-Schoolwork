def school_year(year:int) -> str:
    '''Returns a string stating based off what school year a person is in, if they are in elementary school, middle school or secondary school, along with information such as what grade they're in (i.e. "grade 8") or the name of the grade (i.e. "freshman"). Returns "unknown" if they are in a grade below 0 or above 12.'''
    if year > 12:
        return "unknown"
    elif year >= 9:
        '''
        # tuples not allowed :(
        return f"secondary ({('freshman', 'sophomore', 'junior', 'senior')[year - 9]})"
        '''
        if year - 9 == 0:
            return "secondary (freshman)"
        elif year - 9 == 1:
            return "secondary (sophmore)"
        elif year - 9 == 2:
            return "secondary (junior)"
        elif year - 9 == 3:
            return "secondary (senior)"
    elif year >= 6:
        return f"middle (grade {year})"
    elif year == 0:
        return "kindergarten"
    return f"elementary (grade {year})"