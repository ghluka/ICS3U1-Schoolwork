x = int(input("Give me an int: "))
y = float(input("Give me a float: "))

print(f"{x} + {y} = {x+y:.1f}")
print(f"{x} - {y} = {x-y:.1f}")
print(f"{x} * {y} = {x*y:.1f}")
print(f"{x} / {y} = {x/y:.1f}")
print(f"{x} // {y} = {x//y:.0f}")
print(f"{x}% of {y} = {(x*y)/100:.3f}")