def case_separator(text:str) -> str:
    out = ""
    
    uppers = ""
    lowers = ""
    for c in text:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppers += c
        elif c == " ":
            out += f"{uppers}{lowers}\n"
            uppers = ""
            lowers = ""
        else:
            lowers += c
    out += f"{uppers}{lowers}"
    
    return out