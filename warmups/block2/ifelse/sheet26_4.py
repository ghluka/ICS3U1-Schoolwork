def grade_average(mark_1:int, mark_2:int, mark_3:int) -> str:
    '''Returns a letter grade (F, D, C, B, A) based on the average of 3 marks'''
    average = (mark_1 + mark_2 + mark_3) / 3
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F" 