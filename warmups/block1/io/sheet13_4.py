x = int(input("Give me an int: "))
y = int(input("Give me another int: "))
z = int(input("Give me one more int: "))

avg = (x+y+z)/3
n_spaces = len(f"{avg:.1f}")+2

print(f"+{'-'*n_spaces}+")
print(f"|{x:^{n_spaces}}|")
print(f"|{y:^{n_spaces}}|")
print(f"|{z:^{n_spaces}}|")
print(f"+{'-'*n_spaces}+")
print(f"|{avg:^{n_spaces}.1f}|")
print(f"+{'-'*n_spaces}+")