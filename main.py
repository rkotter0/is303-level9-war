
#Game loop and war logic. Plays rounds between two Player
#objects until one player holds every card.
#Run this file to play:  python main.py

from cards import Deck
from player import Player


# Has a player draw one card, print it, and add it to the pot.
# Returns the card, or None if the player has no cards left.
def draw_for_battle(oPlayer, lstPot):
    if not oPlayer.has_cards():
        return None
    oCard = oPlayer.draw_card()
    lstPot.append(oCard)
    print(f"{oPlayer.name} drew the {oCard}.")
    return oCard


# Prints how many cards each player is holding.
def show_counts(oPlayer1, oPlayer2):
    for oPlayer in [oPlayer1, oPlayer2]:
        iCount = oPlayer.card_count()
        if iCount == 1:
            print(f"{oPlayer.name} has 1 card.")
        else:
            print(f"{oPlayer.name} has {iCount} cards.")


# Plays one round. If the cards tie, the players go to war and keep
# drawing one card each until the cards are different. The winner
# collects every card played during the round (the pot).
def play_round(oPlayer1, oPlayer2):
    lstPot = []   # list of every Card object played this round

    oCard1 = draw_for_battle(oPlayer1, lstPot)
    oCard2 = draw_for_battle(oPlayer2, lstPot)

    bWar = False
    while oCard1.rank == oCard2.rank:
        print("War!")
        bWar = True
        oCard1 = draw_for_battle(oPlayer1, lstPot)
        oCard2 = draw_for_battle(oPlayer2, lstPot)

        # A player who can't draw during a war loses, and the other
        # player collects the pot
        if oCard1 is None and oCard2 is None:
            print("Both players ran out of cards during the war!")
            return
        elif oCard1 is None:
            print(f"{oPlayer1.name} ran out of cards during the war!")
            oPlayer2.add_cards(lstPot)
            return
        elif oCard2 is None:
            print(f"{oPlayer2.name} ran out of cards during the war!")
            oPlayer1.add_cards(lstPot)
            return

    if oCard1.rank > oCard2.rank:
        oWinner = oPlayer1
    else:
        oWinner = oPlayer2

    if bWar:
        print(f"{oWinner.name} wins the war!")
    else:
        print(f"{oWinner.name} wins the round!")

    # add_cards() shuffles the pot before adding it to the winner's hand
    oWinner.add_cards(lstPot)


# Asks the player to continue. Returns True if they typed 'a' to
# auto-play the rest of the game. If input is closed (Ctrl-D) or the
# player presses Ctrl-C, the game finishes on auto-play instead of crashing.
def ask_to_continue():
    try:
        sChoice = input("Press Enter to play the next round (or 'a' to auto-play). ")
    except (EOFError, KeyboardInterrupt):
        print("\nFinishing the game on auto-play.")
        return True
    return sChoice.strip().lower() == "a"


# Sets up two decks and two players, then plays rounds until one
# player has collected all of the cards.
def play_game():
    print("Welcome to Two-Deck War!")
    print("A full game can take thousands of rounds. Type 'a' at any prompt to auto-play to the end.\n")

    # Two separate Deck objects, one for each player, shuffled before play
    oDeck1 = Deck()
    oDeck2 = Deck()
    oDeck1.shuffle()
    oDeck2.shuffle()

    # Two Player objects, each dealt their own deck
    oPlayer1 = Player("Player 1", oDeck1.deal())
    oPlayer2 = Player("Player 2", oDeck2.deal())

    bAutoPlay = False
    iRound = 0

    # Game loop: keep playing while both players still have cards
    while oPlayer1.has_cards() and oPlayer2.has_cards():
        iRound += 1
        print(f"--- Round {iRound} ---")
        play_round(oPlayer1, oPlayer2)
        show_counts(oPlayer1, oPlayer2)

        bGameOver = not oPlayer1.has_cards() or not oPlayer2.has_cards()
        if not bAutoPlay and not bGameOver:
            bAutoPlay = ask_to_continue()
        print()

    # Final message identifying the winner
    if oPlayer1.has_cards():
        oWinner = oPlayer1
    elif oPlayer2.has_cards():
        oWinner = oPlayer2
    else:
        oWinner = None

    if oWinner is None:
        print("Neither player has any cards left. The game is a tie!")
    else:
        print(f"{oWinner.name} has collected all of the cards.")
        print(f"{oWinner.name} wins the game after {iRound} rounds!")


# Start the game
play_game()
