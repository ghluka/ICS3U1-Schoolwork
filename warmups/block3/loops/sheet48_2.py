def boxify(text:str, size:int) -> str:
    out = ''

    i = 1 # i wish i could just use enumerate :(
    for c in text:
        out += c
        if i % size == 0:
            out += '\n'
        i += 1

    return out