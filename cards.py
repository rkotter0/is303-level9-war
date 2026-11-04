# cards.py
# This file has the Card class and the Deck class for our War game.

import random


class Card:
    # A Card has a rank (2-14) and a suit (Hearts, Diamonds, Clubs, Spades).
    # Face cards use numbers so they are easy to compare:
    # 11 = Jack, 12 = Queen, 13 = King, 14 = Ace
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # This controls what prints when we print a card, like "Queen of Clubs"
    def __str__(self):
        if self.rank == 11:
            name = "Jack"
        elif self.rank == 12:
            name = "Queen"
        elif self.rank == 13:
            name = "King"
        elif self.rank == 14:
            name = "Ace"
        else:
            name = str(self.rank)
        return name + " of " + self.suit


class Deck:
    # A Deck starts with all 52 cards in a list
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for suit in suits:
            for rank in range(2, 15):  # 2 through 14
                new_card = Card(rank, suit)
                self.cards.append(new_card)

    # Mixes up the cards in the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Gives back the list of cards so a player can use them as their hand
    def deal(self):
        return self.cards
