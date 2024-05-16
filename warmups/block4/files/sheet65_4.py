def count_letter_in_file(path:str) -> int:
    in_file = open(path)
    
    lines = 0
    for line in in_file:
        line = line.strip()
        if not line.startswith("#") and len(line) > 0:
            lines += 1
    
    in_file.close()
    
    return lines