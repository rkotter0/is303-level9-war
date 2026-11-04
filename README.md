# is303-level9-war
IS 303 Level 9: Two-Deck War card game

## How to run

```
python main.py
```

Press Enter to play each round. A full game usually takes 1,000–6,000 rounds, so type `a` at any prompt to auto-play to the end.

## Files

| File | Contents |
| --- | --- |
| `cards.py` | `Card` and `Deck` classes |
| `player.py` | `Player` class |
| `main.py` | Game loop and war logic (run this file) |
| `test_war.py` | Tests for normal rounds, ties, repeated ties and the end of the game |

## Rules as programmed

- Each player gets their own shuffled 52-card deck (104 cards total). Ace is high.
- Each round, both players draw a card. The higher card wins both cards.
- On a tie, the players go to war: each draws one more card. Ties keep going until someone wins, and the winner takes every card played that round.
- If a player runs out of cards during a war, they lose and the other player takes the cards.
- The game ends when one player has all of the cards.

## Choices we made

- **Won cards are shuffled** (in `Player.add_cards`) before going to the bottom of the winner's hand. Without this, the same card order can repeat and the game may never end.
- **Auto-play (`a`)** exists because pressing Enter thousands of times isn't practical.
- **Ctrl-D or Ctrl-C** at the prompt switches to auto-play instead of crashing (handled with `try`/`except`).

## Testing

Run `python test_war.py`. It stacks each player's hand to force specific situations and prints PASS or FAIL for each:

1. Normal round (9 vs 4)
2. Single tie (Queen vs Queen, then 7 vs 3)
3. Repeated tie (5 vs 5, 8 vs 8, then 2 vs King)
4. Player runs out of cards during a war
5. Both players run out in the same war
6. 20 full games played to the end, each finishing with one player holding all 104 cards
