#Write a program that 'spins' a random spinner from 1 - 50
#until it gets a 25, and then outputs how many spins it took.

#Also, it will output the set of all spins above 25,
#and all that were below 25.   *building up string!

#Also, determine what the highest of all the spins was....


'''
Sample Execution Output:

It took 20 spins to get a 25.
Above 25: 34, 34, 48, 38, 33, 37, 43, 26, 26, 26, 41, 44, 43 
Below 25: 24, 4, 24, 10, 12, 10 
Highest overall spin was a 48

'''

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