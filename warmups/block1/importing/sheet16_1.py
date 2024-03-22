import math

numer = int(input("Numerator: "))
denom = int(input("Denominator: "))

gcd = math.gcd(numer, denom)

print(f"{int(numer/gcd)}/{int(denom/gcd)}")