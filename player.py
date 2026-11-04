# player.py
# This file has the Player class for our War game.

import random


class Player:
    # A Player has a name and a hand (a list of Card objects)
    def __init__(self, name, cards):
        self.name = name
        self.hand = cards

    # Takes the top card off the player's hand and returns it
    def draw_card(self):
        return self.hand.pop(0)

    # Puts the cards the player won on the bottom of their hand.
    # We shuffle the won cards first so the game doesn't get stuck
    # repeating the same rounds forever.
    def add_cards(self, cards):
        random.shuffle(cards)
        for card in cards:
            self.hand.append(card)

    # Returns how many cards the player has
    def card_count(self):
        return len(self.hand)

    # Returns True if the player still has cards, False if they are out
    def has_cards(self):
        return len(self.hand) > 0
