def file_average(path:str) -> float:
    in_file = open(path)
    lines = in_file.readlines()
    
    avg = 0
    for n in lines:
        avg += float(n)
    avg /= len(lines)
    
    in_file.close()
    
    return avg