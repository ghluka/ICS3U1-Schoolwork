file = open("test.txt")
lines = file.readlines()
file.close()

numbers = []
for line in lines:
    numbers.append(float(line.strip()))

numbers.append(1.0)
numbers.sort()
positives = numbers[numbers.index(1):]
positives.remove(1)
not_positives = numbers[:numbers.index(1)]


def squares(numbers:list) -> list:
    squared_numbers = []
    
    for num in numbers:
        squared_numbers.append(num ** 2)
    
    return squared_numbers