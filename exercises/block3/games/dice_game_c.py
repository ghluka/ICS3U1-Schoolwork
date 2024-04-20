from random import randrange

#your code below

def dice_game(rounds:int) -> str:
   out = ""
   total_points = 0

   for i in range(rounds):
      round = ""

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
            round += f"\n{roll_1},{roll_2}: DONE"
         else:
            round += f"\n{roll_1},{roll_2}: {points}"
      
      if i > 0:
         out += "\n\n"
      out += f"{points} POINTS{round}"
      total_points += points
   
   out += f"\n\nAfter {rounds} rounds: {total_points} points total"

   return out