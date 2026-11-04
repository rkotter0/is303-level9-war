# Author: Abraham Olenslager
# Description: Tests for Two-Deck War. Stacks each player's hand with
#              chosen cards so we can check normal rounds, ties, repeated
#              ties, running out during a war, and full games to the end.
#              Run with:  python test_war.py

import builtins
import contextlib
import io
import random

from cards import Card
from player import Player

# Importing main.py plays one full game, because main.py calls play_game()
# at the bottom. Answer every prompt with 'a' and hide the output so the
# game auto-plays, then keep its output to check the end of the game.
builtins.input = lambda sPrompt="": "a"
random.seed(1)
oFirstGame = io.StringIO()
with contextlib.redirect_stdout(oFirstGame):
    import main
from main import play_round, play_game

iPassed = 0
iFailed = 0


# Prints PASS or FAIL for one check and keeps a running count
def check(sName, bResult):
    global iPassed, iFailed
    if bResult:
        iPassed += 1
        print(f"PASS  {sName}")
    else:
        iFailed += 1
        print(f"FAIL  {sName}")


# Builds two players whose hands hold the given card ranks, top card first
def stacked_players(lstRanks1, lstRanks2):
    lstHand1 = []
    for iRank in lstRanks1:
        lstHand1.append(Card(iRank, "Hearts"))
    lstHand2 = []
    for iRank in lstRanks2:
        lstHand2.append(Card(iRank, "Spades"))
    oPlayer1 = Player("Player 1", lstHand1)
    oPlayer2 = Player("Player 2", lstHand2)
    return oPlayer1, oPlayer2


print("=== Normal round: 9 vs 4 ===")
oP1, oP2 = stacked_players([9, 5], [4, 6])
play_round(oP1, oP2)
check("Player 1 wins and collects both cards", oP1.card_count() == 3 and oP2.card_count() == 1)

print("\n=== Single tie: Queen vs Queen, then 7 vs 3 ===")
oP1, oP2 = stacked_players([12, 7, 2], [12, 3, 2])
play_round(oP1, oP2)
check("Player 1 wins the war and all 4 cards", oP1.card_count() == 5 and oP2.card_count() == 1)

print("\n=== Repeated tie: 5 vs 5, 8 vs 8, then 2 vs King ===")
oP1, oP2 = stacked_players([5, 8, 2], [5, 8, 13])
play_round(oP1, oP2)
check("Player 2 wins all 6 cards", oP2.card_count() == 6 and oP1.card_count() == 0)

print("\n=== Tie on Player 1's last card ===")
oP1, oP2 = stacked_players([10], [10, 4])
play_round(oP1, oP2)
check("Player 1 runs out, Player 2 gets every card", oP1.card_count() == 0 and oP2.card_count() == 3)

print("\n=== Both players run out in the same war ===")
oP1, oP2 = stacked_players([5, 7], [5, 7])
play_round(oP1, oP2)
check("Neither player has cards (game is a tie)", oP1.card_count() == 0 and oP2.card_count() == 0)

print("\n=== End of game: 20 full games on auto-play ===")
iGamesOk = 0
for iSeed in range(20):
    random.seed(iSeed)
    oOutput = io.StringIO()
    with contextlib.redirect_stdout(oOutput):
        play_game()
    sOutput = oOutput.getvalue()
    if "has 104 cards." in sOutput and "has collected all of the cards." in sOutput:
        iGamesOk += 1
check("Every game ends with one player holding all 104 cards", iGamesOk == 20)

print(f"\n{iPassed} passed, {iFailed} failed")
