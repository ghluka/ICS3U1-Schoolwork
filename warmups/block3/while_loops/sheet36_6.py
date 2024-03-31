def gcf(n1:int, n2:int):
    a = abs(n1 - n2)

    while not (n1 % a == n2 % a == 0):
        a -= 1
        
    return a