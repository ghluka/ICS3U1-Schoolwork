def sum_all_digits(digits:str) -> int:
    sum = 0

    for digit in digits:
        sum += int(digit)
    
    return sum