from random import randrange

#your code below

spins = 1
spin = randrange(1, 50 + 1)

above_25 = "Above 25: "
below_25 = "Below 25: "
highest = spin

while spin != 25:
    spin = randrange(1, 50 + 1)
    spins += 1

    if spin < 25:
        if below_25 != "Below 25: ":
            below_25 += ", "
        below_25 += str(spin)
    elif spin > 25:
        if above_25 != "Above 25: ":
            above_25 += ", "
        above_25 += str(spin)
    
    if spin > highest:
        highest = spin

print(f"It took {spins} spins to get a 25.")
print(above_25)
print(below_25)
print(f"Highest overall spin was a {highest}")