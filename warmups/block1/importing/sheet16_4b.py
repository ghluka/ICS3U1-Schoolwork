import math
from trig_functions import sine_inverse

a = float(input("What is the height of your right triangle? "))
b = float(input("What is the base of your right triangle? "))
c = math.hypot(b, a)

alpha = sine_inverse(a/c)
beta = sine_inverse(b/c)

print(f"\nArea: {b*a/2:.3f}")
print(f"Perimeter: {a+b+c:.3f}\n")

print(f"∠α = {alpha:.3f}")
print(f"∠β = {beta:.3f}")