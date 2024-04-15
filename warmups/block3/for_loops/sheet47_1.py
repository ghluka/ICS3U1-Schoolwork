i = input("Input 0: ")
out = ""

while i != "0":
    if out != "":
        out += ", "
    out += i

    i = input("Input 0: ")

print(out)