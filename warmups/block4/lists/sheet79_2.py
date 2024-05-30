# initialize data variables
ids = []

names = []

averages = []
class_average = 0

# store data
f = open("related_lists.txt")
for line in f:
    student_data = line.strip("\n").split(", ")
    
    ids.append(int(student_data[0]))
    
    names.append(student_data[1])
    
    averages.append(int(student_data[2]))
    class_average += int(student_data[2])

f.close()

class_average /= len(averages)

# student selector
print("Students:")
for i in range(1, len(names) + 1):
    name = names[i - 1]
    print(f"{i: >{len(str(len(names)))}}. {name}")
i = int(input("Select a student (by #): ")) - 1

# output data
average = class_average-averages[i]
print(f"{names[i]} (id #{ids[i]}) has a {averages[i]}%", end="")
if average < 0:
    print(f" ({abs(average):.1f}% above class average)")
elif average > 0:
    print(f" ({abs(average):.1f}% below class average)")