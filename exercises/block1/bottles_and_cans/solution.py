# ask questions and type-cast if necessary
name = input("What is your name? ")
balance = float(input("How much money do you have in your wallet already? "))
bottles_under_630ml = int(input("How many bottles under 630 mL? "))
bottles_above_630ml = int(input("How many bottles 630 mL or more? "))
cans = int(input("How many cans? "))

# calculate earnings and total items
total = bottles_under_630ml + bottles_above_630ml + cans
earnings = bottles_under_630ml * .1 + bottles_above_630ml * .2 + cans * .1

# output results
print(f"Thank you {name}")
print(f"You earned ${earnings} from {total} items")
print(f"You now have ${balance+earnings}")