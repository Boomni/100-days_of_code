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

rock_paper_scissors = """
        Rock                              Paper                          Scissors
        _______                        ________                         _______    
    ---'   ____)                   ---'    ____)____                ---'   ____)____
          (_____)                             ______)                         ______)
          (_____)                             _______)                     __________)
          (____)                             _______)                     (____)
    ---.__(___)                    ---.___________)                 ---.__(___)
"""
print("\n{}\n{}{}".format("Welcome".center(90), "To".center(90), rock_paper_scissors))

choice = [rock, paper, scissors]

comp_choice = random.randint(0, 2)
computer = choice[comp_choice]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. :"))
user = choice[user_choice]

draw = "Computer chose {}\nYou chose {}{}"
win = "Computer chose {}\nYou chose {}{}"
loose = "Computer chose {}\nYou chose {}{}"

if comp_choice == user_choice:
    print(draw.format(computer, user, "Its a Draw!".center(90)))
elif comp_choice == 0 and user_choice == 2:
    print(loose.format(computer, user, "You Loose!".center(90)))
elif comp_choice == 0 and user_choice == 1:
    print(win.format(computer, user, "You Win!".center(90)))
elif comp_choice == 2 and user_choice == 1:
    print(loose.format(computer, user, "You Loose!".center(90)))
elif comp_choice == 2 and user_choice == 0:
    print(win.format(computer, user, "You Win!".center(90)))
elif comp_choice == 1 and user_choice == 2:
    print(win.format(computer, user, "You Win!".center(90)))
elif comp_choice == 1 and user_choice == 0:
    print(loose.format(computer, user, "You Loose".center(90)))

print()
print("Game Over!".center(90))
