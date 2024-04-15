def number_trapezoids(n:int) -> str:
    out = ""

    for i in range(0, 10):
        out += f"/{(1 + i) * n}\\"
    
    return out