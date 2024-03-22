def fah_to_cel(fah:float) -> float:
    '''Converts Fahrenheit to Celsius'''
    return (fah - 32) * (5 / 9)

if __name__ == '__main__':
    fahren = float(input("Enter Fahrenheit: "))
    celsius = fah_to_cel(fahren)
    print(f"{fahren}F is {celsius:.1f}C")