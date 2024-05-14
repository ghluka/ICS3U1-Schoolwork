def bumpy(text:str) -> str:
    out = ""
    
    for i in range(0, len(text)):
        if i % 2 == 0:
            out += text[i].lower()
        else:
            out += text[i].upper()
        
    return out