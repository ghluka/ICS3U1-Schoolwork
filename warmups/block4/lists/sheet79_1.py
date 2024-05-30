def farthest_from_origin(xs:list, ys:list) -> float:
    farthest = 0
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        
        d = (x ** 2 + y ** 2) ** .5
        if d > farthest:
            farthest = d
    
    return farthest