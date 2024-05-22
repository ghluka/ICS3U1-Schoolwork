def last_word(text:str) -> str:
    blank_pos = -1
    for i in range(0, len(text)):
        if text[i] == " ":
            blank_pos = i
    out = text[blank_pos + 1:]
    
    return out