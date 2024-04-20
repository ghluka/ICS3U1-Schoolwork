from random import randrange

#your code below

def dice_game() -> str:
   out = ""

   points = 0

   roll_1 = 0
   roll_2 = 1

   while roll_1 != roll_2:
      roll_1 = randrange(1, 6 + 1)
      roll_2 = randrange(1, 6 + 1)

      if abs(roll_1 - roll_2) == 1:
         points += 2
      elif abs(roll_1 - roll_2) == 4:
         points += 3
      if roll_1 + roll_2 == 7:
         points -= 1

      if roll_1 == roll_2:
         out += f"\n{roll_1},{roll_2}: DONE"
      else:
         out += f"\n{roll_1},{roll_2}: {points}"

   out = f"{points} POINTS{out}"

   return out