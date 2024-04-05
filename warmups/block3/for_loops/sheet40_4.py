def pi_ish(end:int) -> float:
    sum = 0

    for i in range(1, end + 1, 2):
        if (i - 1) % 4 == 2:
            sum -= 4 / i
        else:
            sum += 4 / i

    return sum