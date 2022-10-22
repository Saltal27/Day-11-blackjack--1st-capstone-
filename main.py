from replit import clear
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

p1 = random.choice(cards)
p2 = random.choice(cards)
d1 = random.choice(cards)
d2 = random.choice(cards)


def blackjack():
    player_cards = {"p1": p1, "p2": p2}
    player_cards_values = [p1, p2]
    player_cards_summation = p1 + p2
    player_cards_number = 2

    dealer_cards = {"d1": d1, "d2": d2}
    dealer_cards_values = [d1, d2]
    dealer_cards_summation = d1 + d2
    dealer_cards_number = 2

    print(logo)
    print(
        f"Your cards: {player_cards_values}, current score: {player_cards_summation}"
    )
    print(f"Computer's first card: {d1}")

    stand = False
    while not stand:
        hit = input("Type 'y' to get another card, type 'n'to pass:\n").lower()
        if hit == 'y':
            player_cards_number += 1
            player_cards[f"p{player_cards_number}"] = random.choice(cards)

            player_cards_values = []
            for card in player_cards:
                player_cards_values.append(player_cards[card])

            player_cards_summation = 0
            for card in player_cards_values:
                player_cards_summation += card

            print(
                f"Your cards: {player_cards_values}, current score: {player_cards_summation}"
            )
            print(f"Computer's first card: {d1}")

        elif hit == 'n':
            stand = True
            while dealer_cards_summation < 17:
                dealer_cards_number += 1
                dealer_cards[f"d{dealer_cards_number}"] = random.choice(cards)

                dealer_cards_values = []
                for card in dealer_cards:
                    dealer_cards_values.append(dealer_cards[card])

                dealer_cards_summation = 0
                for card in dealer_cards_values:
                    dealer_cards_summation += card

            print(
                f"Your final hand: {player_cards_values}, final score: {player_cards_summation}"
            )
            print(
                f"Computer's final hand: {dealer_cards_values}, final score: {dealer_cards_summation}"
            )
        else:
            print("Invalid info!")


play = input(
    "Do you want to play a game of Blackjack?\nType 'y' or 'n':\n").lower()
if play == 'y':
    clear()
    blackjack()
elif play == 'n':
    print("Understandable. Have a great day (￣^￣)ゞ")
else:
    print("Invalid info!")
