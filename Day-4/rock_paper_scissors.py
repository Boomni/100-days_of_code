
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choice = [Rock, Paper, Scissors]

comp_choice = random.randint(0, 2)
computer = choice[comp_choice]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. :"))
user = choice[user_choice]

draw = "Computer chose {}, you chose {} >>> It's a Draw!"
win = "Computer chose {}, you chose {} >>> You Win!"
loose = "Computer chose {}, you chose {} >>> You Loose!"

if comp_choice == user_choice:
    print(draw.format(computer,user))
elif comp_choice == 0 and user_choice == 2:
    print(loose.format(computer,user))
elif comp_choice == 0 and user_choice == 1:
    print(win.format(computer,user))
elif comp_choice == 2 and user_choice == 1:
    print(loose.format(computer,user))
elif comp_choice == 2 and user_choice == 0:
    print(win.format(computer,user))
elif comp_choice == 1 and user_choice == 2:
    print(win.format(computer,user))
elif comp_choice == 1 and user_choice == 0:
    print(loose.format(computer,user))

print()
print("Game Over!")
