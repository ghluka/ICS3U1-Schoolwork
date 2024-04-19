def factor_chain_2_3(n:int) -> str:
    out = ""

    while n % 3 == 0:
        if out == "":
            out = f"3"
        else:
            out = f"3 x {out}"
        
        n = n / 3

    while n % 2 == 0:
        if out == "":
            out = f"2"
        else:
            out = f"2 x {out}"
        
        n = n / 2
    
    if n == 1:
        return out
    return "N/A"