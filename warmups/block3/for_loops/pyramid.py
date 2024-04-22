def pyramid(n:int) -> str:
    backslash = '\\'

    out = f"{'_': ^{n * 2 + 2}}"
    for i in range(1, n + 1):
        out += f"\n{'/' + ('#' * (i * 2 - 1)) + backslash: ^{n * 2 + 2}}"
    
    return out