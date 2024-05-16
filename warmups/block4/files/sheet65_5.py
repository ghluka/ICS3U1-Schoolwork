def ids_with_digits(path:str, sub:str) -> str:
    in_file = open(path)
    
    ids = ""
    for i in in_file:
        if sub in i:
            ids += f"{i}"
    ids = ids.removesuffix("\n")
    
    in_file.close()
    
    return ids