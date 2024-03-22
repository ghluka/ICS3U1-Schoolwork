name = input("What is your name? ")
age = int(input("What is your age? "))
height = float(input("What is your height (in metres)? "))

print(f"You {name} are {age}y old and {height}m tall")
print(f"You have grown {height/age:.2f}m/y")