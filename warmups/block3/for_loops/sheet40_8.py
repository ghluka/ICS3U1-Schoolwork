def dice_totals(sides_1:int, sides_2:int) -> int:
    sum = 0
    
    for x in range(1, sides_1 + 1):
        for y in range(1, sides_2 + 1):
            #print(f"{x} + {y} = {x + y}")
            sum += x + y
    
    return sum