def union(a:list, b:list) -> list:
    joined = []
    
    for i in range(max([len(a), len(b)])):
        if i < len(a) and not a[i] in joined:
            joined.append(a[i])
        if i < len(b) and not b[i] in joined:
            joined.append(b[i])
    
    return joined