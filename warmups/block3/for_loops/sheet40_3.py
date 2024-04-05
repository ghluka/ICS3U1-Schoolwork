def frac_power_sum(end:int) -> float:
    sum = 0

    for i in range(1, end + 1):
        sum += 1 / 2 ** i

    return sum