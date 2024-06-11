# part 1
names = []
grades = []
fav_colours = []
locations = []

file = open("fake_students.txt")
for student in file:
    student_data = student.split(", ")
    names.append(student_data[0])
    grades.append(int(student_data[1]))
    fav_colours.append(student_data[2])
    locations.append([float(student_data[3]), float(student_data[4])])
file.close()

# part 2
for i in range(1, 13):
    students = grades.count(i)
    if students == 1:
        print(f"Grade {i}: 1 student")
    else:
        print(f"Grade {i}: {students} students")

# part 4
fav_colours.sort(key=fav_colours.count)

# part 3
unique_colours = []
for colour in fav_colours:
    if colour not in unique_colours:
        unique_colours.append(colour)

# part 4
print("\nFAVOURITE COLOUR LEADERBOARD:")
i = 1
for colour in unique_colours:
    likes = fav_colours.count(colour)
    if likes == 1:
        print(f" {i}. {colour}, liked by {likes} student")
    else:
        print(f" {i}. {colour}, liked by {likes} students")
    i += 1