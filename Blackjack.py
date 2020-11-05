import time
from random import randint


def show_card_info(card):
    """shows the card is a user friendly format"""
    return f"{card['name']} {card['suit']}"


def black_jack_setup():
    """Sets the game up by dealing cards and showing them"""
    black_jack.take_bet()
    black_jack.pick_card()
    black_jack.pick_card()
    black_jack.pick_dealer_card()
    black_jack.pick_dealer_card()
    black_jack.show_dealer_card()
    black_jack.check_cards()
    black_jack.show_hand()
    black_jack.check_dealer_cards()


def play_game():
    """plays the game in a loop"""
    print("Welcome to black jack by Joe Leadbeater")
    while black_jack.wallet > 0:
        print("\n--------NEW GAME--------")
        black_jack_setup()
        players_turn()
        if not black_jack.player_bust:
            black_jack.dealers_turn()
        time.sleep(1)
        black_jack.check_winner()
        black_jack.sort_money()
        time.sleep(1.5)
        black_jack.reset_game()


def players_turn():
    """allows the player to pick cards"""
    while black_jack.hand_value < 22:
        message = input("(stick/hit): ")
        if message == "stick":
            black_jack.check_cards()
            print("\nDealers Turn:")
            break
        elif message == "hit":
            time.sleep(1.5)
            black_jack.pick_card()
        else:
            print(f"{message} is an invalid input")
        black_jack.check_cards()
        black_jack.show_hand()
        if black_jack.hand_value > 21:
            print("BUST")
            time.sleep(1)


class Cards:
    def __init__(self):
        self.full_deck = [{'suit': 'Clubs', 'name': 'Ace', 'value': 11}, {'suit': 'Clubs', 'name': 2, 'value': 2},
                          {'suit': 'Clubs', 'name': 3, 'value': 3}, {'suit': 'Clubs', 'name': 4, 'value': 4},
                          {'suit': 'Clubs', 'name': 5, 'value': 5}, {'suit': 'Clubs', 'name': 6, 'value': 6},
                          {'suit': 'Clubs', 'name': 7, 'value': 7}, {'suit': 'Clubs', 'name': 8, 'value': 8},
                          {'suit': 'Clubs', 'name': 9, 'value': 9}, {'suit': 'Clubs', 'name': 10, 'value': 10},
                          {'suit': 'Clubs', 'name': 'Jack', 'value': 10},
                          {'suit': 'Clubs', 'name': 'Queen', 'value': 10},
                          {'suit': 'Clubs', 'name': 'King', 'value': 10},
                          {'suit': 'Diamonds', 'name': 'Ace', 'value': 11},
                          {'suit': 'Diamonds', 'name': 2, 'value': 2}, {'suit': 'Diamonds', 'name': 3, 'value': 3},
                          {'suit': 'Diamonds', 'name': 4, 'value': 4}, {'suit': 'Diamonds', 'name': 5, 'value': 5},
                          {'suit': 'Diamonds', 'name': 6, 'value': 6}, {'suit': 'Diamonds', 'name': 7, 'value': 7},
                          {'suit': 'Diamonds', 'name': 8, 'value': 8}, {'suit': 'Diamonds', 'name': 9, 'value': 9},
                          {'suit': 'Diamonds', 'name': 10, 'value': 10},
                          {'suit': 'Diamonds', 'name': 'Jack', 'value': 10},
                          {'suit': 'Diamonds', 'name': 'Queen', 'value': 10},
                          {'suit': 'Diamonds', 'name': 'King', 'value': 10},
                          {'suit': 'Hearts', 'name': 'Ace', 'value': 11},
                          {'suit': 'Hearts', 'name': 2, 'value': 2}, {'suit': 'Hearts', 'name': 3, 'value': 3},
                          {'suit': 'Hearts', 'name': 4, 'value': 4}, {'suit': 'Hearts', 'name': 5, 'value': 5},
                          {'suit': 'Hearts', 'name': 6, 'value': 6}, {'suit': 'Hearts', 'name': 7, 'value': 7},
                          {'suit': 'Hearts', 'name': 8, 'value': 8}, {'suit': 'Hearts', 'name': 9, 'value': 9},
                          {'suit': 'Hearts', 'name': 10, 'value': 10}, {'suit': 'Hearts', 'name': 'Jack', 'value': 10},
                          {'suit': 'Hearts', 'name': 'Queen', 'value': 10},
                          {'suit': 'Hearts', 'name': 'King', 'value': 10},
                          {'suit': 'Spades', 'name': 'Ace', 'value': 11}, {'suit': 'Spades', 'name': 2, 'value': 2},
                          {'suit': 'Spades', 'name': 3, 'value': 3}, {'suit': 'Spades', 'name': 4, 'value': 4},
                          {'suit': 'Spades', 'name': 5, 'value': 5}, {'suit': 'Spades', 'name': 6, 'value': 6},
                          {'suit': 'Spades', 'name': 7, 'value': 7}, {'suit': 'Spades', 'name': 8, 'value': 8},
                          {'suit': 'Spades', 'name': 9, 'value': 9}, {'suit': 'Spades', 'name': 10, 'value': 10},
                          {'suit': 'Spades', 'name': 'Jack', 'value': 10},
                          {'suit': 'Spades', 'name': 'Queen', 'value': 10},
                          {'suit': 'Spades', 'name': 'King', 'value': 10}]
        self.deck = self.full_deck
        self.hand = []
        self.dealer_hand = []
        self.hand_value = 0
        self.dealer_hand_value = 0
        self.player_bust = False
        self.dealer_bust = False
        self.wallet = 500
        self.pot = 0
        self.win_lose = str

    def take_bet(self):
        """Takes money from the player and adds it to the pot"""
        while True:
            bet = input(f"How much do you want to bet? (cash = £{self.wallet}): ")
            try:
                self.pot = int(bet)
                self.wallet -= self.pot
                break
            except ValueError:
                pass

    def sort_money(self):
        """Gives money if won, or takes it away if lost"""
        if self.win_lose == "lose":
            print(f"£{self.pot} lost")
            self.pot = 0
        elif self.win_lose == "win":
            winnings = 2 * self.pot
            self.pot = 0
            self.wallet += winnings
            print(f"You win £{winnings}")
        elif self.win_lose == "blackjack":
            winnings = (1.5 * self.pot) + self.pot
            self.pot = 0
            self.wallet += winnings
            print(f"You win £{winnings}")

    def check_winner(self):
        """checks to see if player won or lost"""
        win = "\nYOU WIN!!"
        lose = "\nyou lost..."
        if self.player_bust or (self.dealer_hand_value >= self.hand_value and not self.dealer_bust):
            print(lose)
            self.win_lose = "lose"
        elif self.dealer_bust or (self.hand_value > self.hand_value):
            if self.hand_value == 21 and len(self.hand) == 2:
                print("BlackJack!")
                self.win_lose = "blackjack"
            else:
                print(win)
                self.win_lose = "win"

    def reset_game(self):
        """resets the game by putting cards back in the deck"""
        self.deck = self.full_deck
        self.hand = []
        self.dealer_hand = []
        self.hand_value = 0
        self.dealer_hand_value = 0
        self.player_bust = False
        self.dealer_bust = False

    def pick_card(self):
        """takes a card from the deck and gives it to the player"""
        card = self.deck.pop(randint(0, len(self.deck) - 1))
        self.hand.append(card)

    def pick_dealer_card(self):
        """takes a card from he deck and gives it to the dealer"""
        card = self.deck.pop(randint(0, len(self.deck) - 1))
        self.dealer_hand.append(card)

    def show_hand(self):
        """shows the player the cards in their hand"""
        cards = []
        for card in self.hand:
            cards.append(show_card_info(card))
        cards_in_hand = ", ".join(cards)
        print(f"Cards in hand: ({self.hand_value}) {cards_in_hand}")

    def show_dealer_card(self):
        """shows one of the dealers cards"""
        for card in self.dealer_hand:
            card_in_hand = show_card_info(card)
        print(f"\nDealer card: {card_in_hand}\n")

    def show_dealer_hand(self):
        """displays the cards in the dealers hand"""
        cards = []
        for card in self.dealer_hand:
            cards.append(show_card_info(card))
        cards_in_hand = ", ".join(cards)
        print(f"Dealer cards: ({self.dealer_hand_value}) {cards_in_hand}")

    def check_cards(self):
        """checks the value of the players cards to see if bust"""
        hand_value = 0
        for card in self.hand:
            card_value = card['value']
            hand_value += card_value
        for card in self.hand:
            if card['name'] == 'Ace' and hand_value > 21:
                hand_value -= 10
        self.hand_value = hand_value
        if self.hand_value > 21:
            self.player_bust = True

    def check_dealer_cards(self):
        """checks the value of the dealers cards to see if bust"""
        hand_value = 0
        for card in self.dealer_hand:
            card_value = card['value']
            hand_value += card_value
        for card in self.dealer_hand:
            if card['name'] == 'Ace' and hand_value > 21:
                hand_value -= 10
        self.dealer_hand_value = hand_value
        if self.dealer_hand_value > 21:
            self.dealer_bust = True

    def dealers_turn(self):
        """the dealer plays until they win or they reach over 17"""
        self.show_dealer_hand()
        if not self.player_bust:
            while (self.dealer_hand_value < self.hand_value) or (self.dealer_hand_value < 17):
                time.sleep(1.5)
                black_jack.pick_dealer_card()
                black_jack.check_dealer_cards()
                black_jack.show_dealer_hand()


black_jack = Cards()

play_game()
