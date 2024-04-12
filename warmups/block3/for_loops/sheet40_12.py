def sum_alternate_digits(digits:str) -> int:
    sum = 0
    counter = 0

    for character in digits:
        if counter % 2 == 0:
            sum += int(character)
        counter += 1
    
    return sum