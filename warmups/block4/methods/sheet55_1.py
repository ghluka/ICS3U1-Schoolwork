out = ""
text = ""

build = True
while build:
    text = input("Enter text: ")
    if text[0] != "q" and text[0] != "Q":
        out += text[0] + text[-1] + "\n"
    else:
        build = False

out = out[:-1] # remove leading newline

print(out)