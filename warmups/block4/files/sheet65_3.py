def top_student(path:str) -> str:
    in_file = open(path)
    
    highest_student = ""
    highest = 0
    for i in in_file:
        average = float(i.split()[-1])
        if average > highest:
            highest = average
            highest_student = ' '.join(i.split()[:-1])
    
    in_file.close()
    
    return highest_student