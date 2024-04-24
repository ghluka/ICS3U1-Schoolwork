import math

def square_root(number:float) -> float:
    """Calculates the square root of a number using Heron's method"""
    estimate = 5 * 10 ** (math.log(number, 10) / 2 - 1)
    estimate = 1
    while not math.isclose(estimate, number/estimate):
        print(estimate)
        estimate = (estimate + (number / estimate)) / 2

    return estimate

def digit_product_sum(n:int) -> int:
    sum = 0

    for i in str(n):
        for v in str(n):
            sum += int(i) * int(v)
    
    return sum

def text_to_braille(text:str) -> str:
    out = ""

    for c in text:
        if c == "a":
            out += "\u2801"
        elif c == "b":
            out += "\u2803"
        elif c == "c":
            out += "\u2809"
        elif c == "d":
            out += "\u2819"
        elif c == "e":
            out += "\u2811"
        elif c == "f":
            out += "\u280b"
        elif c == "g":
            out += "\u281b"
        elif c == "h":
            out += "\u2813"
        elif c == "i":
            out += "\u280a"
        elif c == "j":
            out += "\u281a"
        elif c == "k":
            out += "\u2805"
        elif c == "l":
            out += "\u2807"
        elif c == "m":
            out += "\u280d"
        elif c == "n":
            out += "\u281d"
        elif c == "o":
            out += "\u2815"
        elif c == "p":
            out += "\u280f"
        elif c == "q":
            out += "\u281f"
        elif c == "r":
            out += "\u2817"
        elif c == "s":
            out += "\u280e"
        elif c == "t":
            out += "\u281e"
        elif c == "u":
            out += "\u2825"
        elif c == "v":
            out += "\u2827"
        elif c == "w":
            out += "\u283d"
        elif c == "x":
            out += "\u282d"
        elif c == "y":
            out += "\u283d"
        elif c == "z":
            out += "\u2835"
        elif c == " ":
            out += " "

    return out

def braille_to_text(text:str) -> str:
    out = ""

    for c in text:
        if c == "\u2801":
            out += "a"
        elif c == "\u2803":
            out += "b"
        elif c == "\u2809":
            out += "c"
        elif c == "\u2819":
            out += "d"
        elif c == "\u2811":
            out += "e"
        elif c == "\u280b":
           out += "f"
        elif c == "\u281b":
            out += "g"
        elif c == "\u2813":
            out += "h"
        elif c == "\u280a":
            out += "i"
        elif c == "\u281a":
            out += "j"
        elif c == "\u2805":
            out += "k"
        elif c == "\u2807":
            out += "l"
        elif c == "\u280d":
            out += "m"
        elif c == "\u281d":
            out += "n"
        elif c == "\u2815":
            out += "o"
        elif c == "\u280f":
            out += "p"
        elif c == "\u281f":
            out += "q"
        elif c == "\u2817":
            out += "r"
        elif c == "\u280e":
            out += "s"
        elif c == "\u281e":
           out += "t"
        elif c == "\u2825":
            out += "u"
        elif c == "\u2827":
            out += "v"
        elif c == "\u283d":
            out += "w"
        elif c == "\u282d":
            out += "x"
        elif c == "\u283d":
            out += "y"
        elif c == "\u2835":
            out += "z"
        elif c == " ":
            out += " " 

    return out

def domino_str(roll_1:int, roll_2:int) -> str:
    out = " " + "_" * 11 + " \n"

    grid_row_1 = "|"
    grid_row_2 = "|"
    grid_row_3 = "|"

    for roll in f"{roll_1}{roll_2}":
        roll = int(roll)

        if roll == 2 or roll == 3:
            grid_row_1 += "\u25cf    "
        elif roll == 4 or roll == 5:
            grid_row_1 += "\u25cf   \u25cf"
            grid_row_3 += "\u25cf   \u25cf"
        elif roll == 6:
            grid_row_1 += "\u25cf \u25cf \u25cf"
            grid_row_3 += "\u25cf \u25cf \u25cf"
        else:
            grid_row_1 += "     "
        grid_row_1 += "|"

        if roll == 1 or roll == 3 or roll == 5:
            grid_row_2 += "  \u25cf  "
        else:
            grid_row_2 += "     "
        grid_row_2 += "|"

        if roll == 2 or roll == 3:
            grid_row_3 += "    \u25cf"
        elif roll != 4 and roll != 5 and roll != 6:
            grid_row_3 += "     "
        grid_row_3 += "|"
    

    out += f"{grid_row_1}\n{grid_row_2}\n{grid_row_3}\n"

    out += " " + f"{chr(8254)}" * 11 + " "
    
    return out

def tree_box(size:int) -> str:
    out = f"+{'-' * size * 2}+\n"
    backslash = "\\"
    
    for i in range(1, size + 1):
        out += f"|{'/' * i: >{size}}{backslash * i: <{size}}|\n"
    for i in range(1, size + 1):
        if i % 2 == 1:
            out += f"|{'|}': ^{size * 2}}|\n"
        else:
            out += f"|{'{|': ^{size * 2}}|\n"
    
    out += f"+{'-' * size * 2}+\n"
    
    return out

