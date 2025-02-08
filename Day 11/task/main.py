import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = True

while play:
    start = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if start == "y":
        print("\n" * 20)
        print(logo)
        dealer_score = 0


        def sum_card(p_lists):
            score = 0
            for card in p_lists:
                score += card
            return score

        p_cards = [random.choice(cards), random.choice(cards)]
        com_cards = [random.choice(cards), random.choice(cards)]
        p_score = sum_card(p_cards)
        com_score = sum_card(com_cards)


        def current_stats():
            print(f"    Your cards: {p_cards}, current score: {p_score}")
            print(f"    Computer's first card: {com_cards[0]}")


        def final_stats():
            print(f"    Your final hand: {p_cards}, final score: {p_score}")
            print(f"    Computer's final hand: {com_cards}, final score: {com_score}")


        def deal_card(lists):
            lists.append(random.choice(cards))
            score = sum_card(lists)
            return score


        current_stats()
        deal_again = True
        while p_score < 21 and deal_again:
            hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if hit == 'y':
                p_score = deal_card(p_cards)
                if p_score > 21:
                    if 11 in p_cards:
                        p_cards[p_cards.index(11)] = 1
                        p_score = sum_card(p_cards)

                else: current_stats()
            else:
                deal_again = False
        deal_on = True
        while com_score < 17 and deal_on:
            com_score = deal_card(com_cards)
            if com_score > 17:
                if com_score > 21:
                    if 11 in com_cards:
                        com_cards[com_cards.index(11)] = 1
                        com_score = sum_card(com_cards)
        if p_score > 21:
            final_stats()
            print("You went over. You lose")

        elif com_score > 21:
            final_stats()
            print("Opponent went over. You win")

        elif com_score > p_score:
            final_stats()
            print("You lose")
        elif p_score > com_score:
            final_stats()
            print("You win")

    else: play = False

