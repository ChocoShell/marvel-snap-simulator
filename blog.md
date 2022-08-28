# Marvel Snap Simulator Development Blog

## 2022-08-27

I created this project to find the best deck in [Marvel Snap].

Marvel Snap is a mobile card game thats played on a board with three locations. The objective of the game is to win two out of three locations. You construct your deck of twelve unique cards and each turn, you and your opponent will play cards which will be revealed at the end of each turn. You start the game with one energy on turn one. Each turn, you gain an additional energy up to the last turn of the game, turn 6. You start with 4 cards in hand and draw a card every turn.

I am going to lay down the ground work for the game first.
This means implementing the board, a deck, the rounds, and the turns.

Downloaded Card Database from [MarvelSnap.io]

### Final Thoughts

Implemented a lot of the groundwork. The program will play a game vs 2 players with a dumb AI. The decks are identical and only have cards that have no abilities.
The code is very messy.
The next step is adding in a card with an effect.

[marvel snap]: https://www.marvelsnap.com/
[marvelsnap.io]: (https://marvelsnap.io/card-database/)
