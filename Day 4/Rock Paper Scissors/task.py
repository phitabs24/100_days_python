from random import choice, random

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

options = [rock, paper, scissors]
my_choice = options[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))]
computer_choice = choice(options)
print(my_choice)
print("Computer chose:")
print(computer_choice)

if my_choice == rock:
    if computer_choice == scissors:
        print("You win")
    elif computer_choice == paper:
        print("You lose")
    else:
        print("It's a draw")
if my_choice == paper:
    if computer_choice == rock:
        print("You win")
    elif computer_choice == scissors:
        print("You lose")
    else:
        print("It's a draw")
if my_choice == scissors:
    if computer_choice == paper:
        print("You win")
    elif computer_choice == rock:
        print("You lose")
    else:
        print("It's a draw")