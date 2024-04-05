def range_sum(start:int, end:int) -> int:
    step = 1
    if end < start:
        step = -1

    sum = 0

    for i in range(start, end + step, step):
        sum += i

    return sum