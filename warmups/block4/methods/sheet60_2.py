def no_upper(text:str) -> str:
    out = ""
    
    for c in text:
        if not c.isupper():
            out += c 
    
    return out