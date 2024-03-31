def fibonacci(end:int):
    a = 0
    b = 1
    
    while b < end:
        b = b + a
        a = b - a
    
    return a