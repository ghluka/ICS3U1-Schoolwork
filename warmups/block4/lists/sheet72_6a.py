def intersection(a:list, b:list) -> list:
    matching = []
    
    for i in a:
        if i in b and i not in matching:
            matching.append(i)
            
    return matching