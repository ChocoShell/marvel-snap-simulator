from .ai import DumbAIMixin


class Player(DumbAIMixin):
    def __init__(self, name: str, deck):
        self.name = name
        self.deck = deck
        self.hand = []

    def draw_starting_hand(self):
        self.hand = self.deck.draw(3)

    def take_turn(self, game):
        self.hand += self.deck.draw()
        print(f"\t{self}'s hand: {self.hand}")
        return self.play(game)

    def __repr__(self):
        return f"{self.name}"
