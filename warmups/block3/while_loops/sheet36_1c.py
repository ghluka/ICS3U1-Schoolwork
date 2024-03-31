# Name greeting
name = input("What is your name?: ")
while name == "": name = input("What is your name?: ")
print(f"Greetings, {name}.")

# Average calculator
sum_of_values = 0
num_of_values = 0

mark = input("Input a mark (enter \"quit\" to stop): ")

while mark != "quit":
    if float(mark) < 0:
        print("Invalid! Grade cannot be below 0%")
    elif float(mark) > 100:
        print("Invalid! Grade cannot be above 100%")
    else:
        sum_of_values += float(mark)
        num_of_values += 1
    
    mark = input("Input a mark (enter \"quit\" to stop): ")

if num_of_values > 0:
    print(f"Your average: {sum_of_values/num_of_values}%")
else:
    print("Unable to get average! No marks entered.")