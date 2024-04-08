# Name greeting
name = input("What is your name?: ")
while name == "": name = input("What is your name?: ")
print(f"Greetings, {name}.")

# Average calculator
sum_of_values = 0
num_of_values = int(input("How many marks do you want to average: "))

for i in range(num_of_values):
    mark = float(input("Input a mark: "))
    while mark < 0 or mark > 100:
        if mark < 0:
            print("Invalid! Grade cannot be below 0%")
        elif mark > 100:
            print("Invalid! Grade cannot be above 100%")
        mark = float(input("Input a mark: "))

    sum_of_values += mark

if num_of_values > 0:
    print(f"Your average: {sum_of_values/num_of_values}%")
else:
    print("Unable to get average! No marks entered.")