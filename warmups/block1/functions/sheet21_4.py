from math import pi

def cylinder_surface(r:float, h:float) -> float:
    '''Returns the surface area of a cylinder with the given radius and height'''
    return 2 * pi * r ** 2 + 2 * pi * r * h

if __name__ == '__main__':
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))
    area_1 = cylinder_surface(radius, height)
    area_2 = cylinder_surface(2*radius, 2*height)
    print(f"Cylinder with r={radius} & h={height} has SA={area_1:.2f}")
    print(f"If double the radius & height, SA={area_2:.2f}")