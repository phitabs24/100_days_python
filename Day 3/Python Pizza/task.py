print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill = 0

if size == "s":
    bill += 15
    if pepperoni == "y":
        bill += 2
if size == "m":
    bill += 20
    if pepperoni == "y":
        bill += 3
if size == "l":
    bill += 25
    if pepperoni == "y":
        bill += 3
if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")