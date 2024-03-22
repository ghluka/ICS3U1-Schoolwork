name = input("What is your name? ")
x = float(input("First argument: ")) # 12.3456
y = float(input("Second argument: ")) # 78.962144

midpoint = (x+y)/2

print("-"*22)
print(f"|{name:^20}|")
print("-"*22)
print(f"Midpoint is {midpoint:.1f}")
print(f"(or {midpoint:.3f} or {midpoint:.0f})")