# 1)
def formula(a:int, b:int) -> float:
    return ((2 * a + 3 * b) ** ((a - b) / 2) / (a * b))


# 2)
def in_order_str(a:int, b:int, c:int) -> str:
    n = [a, b, c]
    n.sort()
    
    out = f"{n[0]}<"
    if n[0] == n[1]:
        out += "="
    out += f"{n[1]}<"
    if n[1] == n[2]:
        out += "="
    out += f"{n[2]}"
    
    return out


# 3)
def rearrange(text:str) -> str:
    numbers = ""
    vowels = ""
    letters = ""

    for c in text.upper():
        if c.isnumeric():
            numbers += c
        elif c in "AEIOU":
            vowels += c
        elif c.isalpha():
            letters += c
    
    return f"{numbers}{vowels}{letters}"


# 4)
"""
    a) Name 3 variable types
        - Integer (int)
        - Float (float)
        - String literal (str)
    b) Name 3 boolean operators
        - and
        - or
        - not
    c) Name 3 relational operators
        - less than (<)
        - greater than (>)
        - equals (==)
"""

if __name__ == "__main__":
# 5)
    # a)
    out = ""
    line = input()
    while len(line.replace(" ", "")) >= 5:
        out += f"{line}\n"
        line = input()
    out = out.removesuffix("\n")

    print(out)

    # b)
    out = ""
    for i in range(8):
        line = input()
        if len(line.replace(" ", "")) >= 5:
            out += f"{line}\n"
    out = out.removesuffix("\n")

    print(out)

# 6)
    file = open("letters.txt")
    
    letters = []
    quantities = []

    for line in file:
        letters.append(line[0])
        quantities.append(int(line[1:]))

    print("Total number of letter-quantity pairs:", len(quantities))
    print("Total quantity of letters:", sum(quantities))
    print("Letter with the highest quantity:", letters[quantities.index(max(quantities))])
    
    total_vowels = 0
    for vowel in "AEIOU":
        total_vowels += quantities[letters.index(vowel)]
    print("Total quantity of all vowels:", total_vowels)

    file.close()

# 7)
"""
    A for-loop by character loops through every character in a string,
    while a for-loop by position loops through every index in a string.

    Example of a for-loop by character:
    >>> for c in text:
    >>>     print(c)

    Example of a for-loop by position:
    >>> for i in range(len(text)):
    >>>     print(text[i])
"""