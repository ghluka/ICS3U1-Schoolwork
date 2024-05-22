def numeric_alpha(text:str) -> str:
    alpha = ""
    numeric = ""
    
    for c in text:
        if c.isalpha():
            alpha += c
        elif c.isnumeric():
            numeric += c
    
    return f"{numeric}{alpha}"