from replit import clear
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
  p1 = random.choice(cards)
  p2 = random.choice(cards)
  d1 = random.choice(cards)
  d2 = random.choice(cards)
  
  player_cards = {"p1": p1, "p2": p2}
  player_cards_values = [p1, p2]
  player_cards_summation = p1 + p2
  player_cards_number = 2

  dealer_cards = {"d1": d1, "d2": d2}
  dealer_cards_values = [d1, d2]
  dealer_cards_summation = d1 + d2
  dealer_cards_number = 2

  print(logo)
  print(f" Your cards: {player_cards_values}, current score: {player_cards_summation}")
  print(f" Computer's first card: {d1}")

  stand = False
  while stand == False and player_cards_summation <= 21:
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

      if player_cards_summation > 21 and 11 in player_cards_values:
        ace_position = player_cards_values.index(11)
        player_cards_values[ace_position] = 1
        player_cards_summation -= 10
        first_ace = True
        while first_ace == True:
          for card in player_cards:
            if player_cards[card] == 11:
              player_cards[card] = 1
              first_ace = False

      print(f" Your cards: {player_cards_values}, current score: {player_cards_summation}")
      print(f" Computer's first card: {d1}")

    elif hit == 'n':
      stand = True
    else:
      print(" Invalid info!")

  while dealer_cards_summation < 17:
    dealer_cards_number += 1
    dealer_cards[f"d{dealer_cards_number}"] = random.choice(cards)

    dealer_cards_values = []
    for card in dealer_cards:
      dealer_cards_values.append(dealer_cards[card])

    dealer_cards_summation = 0
    for card in dealer_cards_values:
      dealer_cards_summation += card

    if dealer_cards_summation > 21 and 11 in dealer_cards_values:
      ace_position = dealer_cards_values.index(11)
      dealer_cards_values[ace_position] = 1
      dealer_cards_summation -= 10
      first_ace = True
      while first_ace == True:
        for card in dealer_cards:
          if dealer_cards[card] == 11:
            dealer_cards[card] = 1
            first_ace = False

  print(f" Your final hand: {player_cards_values}, final score: {player_cards_summation}")
  print(f" Computer's final hand: {dealer_cards_values}, final score: {dealer_cards_summation}")

  if player_cards_summation > 21:
    print("You went over.\nYou lose :(")
  else:
    if dealer_cards_summation > 21:
      print("Opponent went over.\nYou win :)")
    else:
      if player_cards_summation > dealer_cards_summation:
        print("You win ツ")
      elif player_cards_summation == dealer_cards_summation:
        print("Tie *_*")
      else:
        print("You lose (╥﹏╥)")

  again = input("Do you want to play another game of blackjack?\nType 'y' or 'n':\n").lower()
  if again == 'y':
    clear()
    blackjack()
  elif again == 'n':
    print("Understandable. Have a great day ╍●‿●╍")
  else:
    print("Invalid info!")


play = input("Do you want to play a game of Blackjack?\nType 'y' or 'n':\n").lower()
if play == 'y':
  clear()
  blackjack()
elif play == 'n':
  print("Understandable. Have a great day ╍●‿●╍")
else:
  print("Invalid info!")