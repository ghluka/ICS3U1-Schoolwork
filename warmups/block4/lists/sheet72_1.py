marks = []

mark = float(input("Enter a mark (-1 to stop): "))
while mark >= 0:
    marks.append(mark)
    mark = float(input("Enter a mark (-1 to stop): "))

marks.sort()

print("Largest mark:", max(marks))

print("Smallest mark:", min(marks))

mid = len(marks) // 2
## "~" operator wasn't taught :(
#print("Median mark:", (marks[mid] + marks[~mid]) / 2)
if len(marks) % 2 == 0:
    print("Median mark:", (marks[mid] + marks[mid - 1]) / 2)
else:
    print("Median mark:", marks[mid])