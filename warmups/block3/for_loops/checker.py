def checker(n:int) -> str:
    out = ""

    even = f"{chr(9608)}{chr(9608)}  " * (n - n // 2)
    odd = f"  {chr(9608)}{chr(9608)}" * (n // 2)

    for i in range(n):
        if i > 0:
            out += '\n'
        if i % 2 == 0:
            out += even
        else:
            out += odd

    return out