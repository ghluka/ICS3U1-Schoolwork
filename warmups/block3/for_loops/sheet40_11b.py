def sum_all_digits(digits:str) -> int:
    sum = 0
    negative = False

    for digit in digits:
        if digit == "-":
            negative = True
        elif negative:
            sum -= int(digit)
            negative = False
        else:
            sum += int(digit)
    
    return sum