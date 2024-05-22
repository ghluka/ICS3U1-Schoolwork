def mirror(numbers:list) -> list:
    for n in reversed(numbers):
        numbers.append(n)
    
    return numbers