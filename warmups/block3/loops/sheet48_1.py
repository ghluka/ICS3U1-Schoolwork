import random

def even_odd(size:int) -> str:
    r = str(random.randrange(10 * size, int('9' * size) + 1))
    
    odd = ""
    even = ""

    for c in r:
        if int(c) % 2 == 0:
            even += c
        else:
            odd += c

    return even + odd