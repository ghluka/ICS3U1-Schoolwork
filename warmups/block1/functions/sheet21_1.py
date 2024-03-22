from random import randint

def roll_2_dice(sides:int) -> int:
    '''Returns the sum of two die rolled with a given number of sides in a formatted string'''
    return randint(1, sides) + randint(1, sides)

if __name__ == '__main__':
    sides = int(input("How many sides are on the dice? "))
    total = roll_2_dice(sides)
    print(f"Roll total = {total}")