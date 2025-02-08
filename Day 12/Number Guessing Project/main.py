from art import logo
from random import randint
print(logo)

print("Welcome to the number guessing game\nI'm thinking of a number between 1 and 100")
is_game_on: bool = True
CORRECT_VALUE: int = randint(1, 100)
difficulty: str = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    lives_left: int = 10
else:
    lives_left: int = 5

while is_game_on:
    print(f"You have {lives_left} attempts remaining to guess the number.")
    guess_value: int = int(input("Make a guess: "))
    if guess_value == CORRECT_VALUE:
        print(f"You got it! The answer was {CORRECT_VALUE}.")
        is_game_on = False
    else:
        lives_left -= 1
        if lives_left < 1:
            print("You've run out of guesses. You lose.")
            print(f"The correct answer was {CORRECT_VALUE}")
            is_game_on = False
        else:
            if guess_value < CORRECT_VALUE:
                print("Too low.\nGuess again.")
            elif guess_value > CORRECT_VALUE:
                print("Too high.\nGuess again.")
