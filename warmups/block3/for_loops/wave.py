def waves(end:int, pattern:str) -> None:
    for x in range(1, end):
        for c in pattern:
            for y in range(x):
                print(f"{y * ' '}{c}")
            for y in range(x, -1, -1):
                print(f"{y * ' '}{c}")