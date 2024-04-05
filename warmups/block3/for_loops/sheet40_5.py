def num_spaces(string:str) -> int:
    spaces = 0

    for i in string:
        if i == " ":
            spaces += 1

    return spaces