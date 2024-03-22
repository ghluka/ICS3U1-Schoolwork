import math

a = float(input("What is the height of your right triangle? "))
b = float(input("What is the base of your right triangle? "))
c = math.hypot(b, a)

print(f"\nArea: {b*a/2:.3f}")
print(f"Perimeter: {a+b+c:.3f}")