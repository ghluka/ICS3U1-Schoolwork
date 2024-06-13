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
    print(f"Grade {i}: {students} students")

# part 3
unique_colours = []
for colour in fav_colours:
    if colour not in unique_colours:
        unique_colours.append(colour)

# part 4
colour_likes = []
for colour in unique_colours:
    likes = fav_colours.count(colour)
    colour_likes.append(likes)
colour_likes.sort()
colour_likes.reverse()

print("\nFAVOURITE COLOUR LEADERBOARD:")
i = 1
for likes in colour_likes:
    for colour in unique_colours:
        if fav_colours.count(colour) == likes:
            print(f"{i}. {colour}, liked by {likes} students")
    i += 1