id = input("ID #: ")
i = 1

out = ""

while id != "":
    first_name = input("First name: ")
    last_name = input("Last name: ")

    out += f"{i}. {id}\t{last_name}, {first_name}\n"
    i += 1

    id = input("ID #: ")

print(out)