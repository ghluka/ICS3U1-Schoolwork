def name_swap(name:str) -> str:
    i = 0
    while i < len(name) and name[i] != " ":
        i += 1
    
    out = ""
    if len(name) != i:
        out = f"{name[i + 1:]}, "
    out += f"{name[:i]}"

    return out