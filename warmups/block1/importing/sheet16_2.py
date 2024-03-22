from random import randrange as random
from time import sleep

roll1, roll2, roll3, roll4 = random(0, 6), random(0, 6), random(0, 6), random(0, 6)

print(f"[{roll1}]")
sleep(1.5)
print(f"[{roll1}][{roll2}]")
sleep(1.5)
print(f"[{roll1}][{roll2}][{roll3}]")
sleep(1.5)
print(f"[{roll1}][{roll2}][{roll3}][{roll4}]")