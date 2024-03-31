# Name greeting
name = input("What is your name?: ")
while name == "": name = input("What is your name?: ")
print(f"Greetings, {name}.")

# Average calculator
sum_of_values = 0
num_of_values = 0

mark = float(input("Input a mark (enter -1 to stop): "))

while mark != -1:
    sum_of_values += mark
    num_of_values += 1
    mark = float(input("Input a mark (enter -1 to stop): "))

if num_of_values > 0:
    print(f"Your average: {sum_of_values/num_of_values}%")
else:
    print("Unable to get average! No marks entered.")