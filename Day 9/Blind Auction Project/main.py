from art import logo
print(logo)
import os

def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Unix-based
    else:
        os.system('clear')




# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
#
add_bid = True
bids = {}
while add_bid:
    name = input("What is your name?: ")
    bid = float(input("What is your bid? $"))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == "no":
        add_bid = False
    clear_screen()

highest_bid = 0
winner = ""

for key in bids:
    if highest_bid < bids[key]:
        highest_bid = bids[key]
        winner = key

print(f"The winner is {winner} with a bid of {highest_bid} ")



