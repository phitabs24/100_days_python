import art
import random
from game_data import data

print(art.logo)



def guess_is_correct():
    if guess == 'a':
        if a_rank > b_rank:
            return True
    elif guess == 'b':
        if b_rank > a_rank:
            return True



game_on: bool = True
score: int = 0

while game_on:

    a: dict = random.choice(data)
    b: dict = random.choice(data)

    while a == b:
        b = random.choice(data)

    a_rank: int = a['follower_count']
    b_rank: int = b['follower_count']

    # print(f"a = {a_rank}, b = {b_rank}")

    print(f"""Compare A: {a['name']}, a {a['description']} from {a['country']}.\n{art.vs}\nAgainst B: {b['name']}, a {b['description']} from {b['country']}""")
    keep_guessing = True
    while keep_guessing:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == 'a' or guess == 'b':
            keep_guessing = False
        else:
            print(f"'{guess.upper()}' not recognise. Please enter a valid choice")

    if guess_is_correct():
        score += 1
        print(f"You're right! Current score: {score}\n")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False

