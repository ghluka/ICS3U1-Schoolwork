def get_complement(dna:str) -> str:
    out = ""

    for c in dna:
        if c == "G":
            out += f"C"
        elif c == "C":
            out += f"G"
        elif c == "A":
            out += f"T"
        elif c == "T":
            out += f"A"
    
    return out