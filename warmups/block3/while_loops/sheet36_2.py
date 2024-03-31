import time
import random

numbers = 0
even = 0
odd = 0

start = time.perf_counter()

n = random.randrange(0, 1_000_001)
while n != 1_000_000:
    numbers += 1
    
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    
    n = random.randrange(0, 1_000_001)

elapsed = time.perf_counter() - start

print(f"{numbers} random numbers were picked before picking 1000000")
print(f"{even} were even, {odd} were odd")
print(f"The whole process took {elapsed:.2f} seconds")