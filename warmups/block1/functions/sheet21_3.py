def make_equation_str(m:float, x:int, y:int) -> str:
    '''Converts a line into a slope-intercept formula into a formatted string'''
    b = y - m * x
    return f'y = {slope}x {f"+ {b}" if b >= 0 else f"- {abs(b)}"}'

if __name__ == '__main__':
    slope = float(input("Enter slope: "))
    x_coord = int(input("Enter x-coord: "))
    y_coord = int(input("Enter y-coord: "))
    equation_string = make_equation_str(slope, x_coord, y_coord)
    print(f"Your equation is {equation_string}")