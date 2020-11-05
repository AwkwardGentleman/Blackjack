import random

deck = []


def check_picture_card(number):
    """assigns a picture to the card"""
    if number == 1:
        return "Ace"
    elif number == 11:
        return "Jack"
    elif number == 12:
        return "Queen"
    elif number == 13:
        return "King"
    else:
        return number


def check_value(number):
    """checks the value, turning 1 to 11 and values over 10 to 10"""
    if number >= 10:
        return 10
    if number == 1:
        return 11
    else:
        return number


def check_suit(number):
    """assigns a suit to the card"""
    if number == 1:
        return "Clubs"
    elif number == 2:
        return "Diamonds"
    elif number == 3:
        return "Hearts"
    elif number == 4:
        return "Spades"


def make_deck():
    """makes the deck"""
    for j in range(1, 5):
        for i in range(1, 14):
            card_name = check_picture_card(i)
            card_value = check_value(i)
            card_suit = check_suit(j)
            card = {"suit": card_suit, "name": card_name, "value": card_value}
            deck.append(card)


make_deck()
print(deck)