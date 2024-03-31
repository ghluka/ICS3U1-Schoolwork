def perfect_squares(end:int):
    n = 1
    while n ** 2 < end:
        print(f"{n}{chr(178)} = {n**2}")
        n += 1