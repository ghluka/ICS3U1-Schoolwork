file = open("grades.txt")
student_data = file.readlines()
file.close()

names = []
marks = []

for student in student_data:
    names.append(student.split(", ", 1)[0])
    
    grades = []
    for grade in student.strip().split(", ")[1:]:
       grades.append(int(grade))
    marks.append(grades) 

width = len(max(names, key=len))

print(f"+{'-'*(width + 23)}+")
print(f"|   {'NAME': <{width}}   | AVG  | LO | HI |")
print(f"+{'-'*(width + 23)}+")

lowest = 100
highest = 0

for i in range(len(names)):
    name = names[i]
    grades = marks[i]
    
    low = min(grades)
    if lowest > low:
        lowest = low
    high = max(grades)
    if highest < high:
        highest = high
    average = sum(grades) / len(grades)
    
    print(f"|   {name: <{width}}   |{average: ^6.1f}|{low: ^4}|{high: ^4}|")
    
print(f"+{'-'*(width + 23)}+")
print(f"|   {'OVERALL': >{width + 9}} |{lowest: ^4}|{highest: ^4}|")
print(f"+{'-'*(width + 23)}+")