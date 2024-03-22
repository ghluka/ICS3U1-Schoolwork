def to_feet(inches:int) -> str:
    '''Returns the number of feet from inches in a formatted string'''
    return f'{inches//12}ft_{inches%12}in'

if __name__ == '__main__':
    inches = int(input("Enter inches: "))
    feet = to_feet(inches)
    print(f"{inches}in is {feet}")