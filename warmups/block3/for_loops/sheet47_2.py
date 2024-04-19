def text_block(string:str) -> str:
    out = ""

    # [out := f"{out}{s*len(string)}\n" for s in string]
    for s in string:
        out += f"{s * len(string)}\n"

    return out