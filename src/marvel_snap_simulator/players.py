from .ai import DumbAIMixin
from .cards import Card


HAND_LIMIT = 7


class Player(DumbAIMixin):
    def __init__(self, name: str, deck):
        self.name = name
        self.deck = deck
        self.hand = []

    def draw_starting_hand(self):
        for card in self.deck.draw(3):
            self.add_card_to_hand(card)

    def take_turn(self, game):
        card = self.deck.draw()
        if card:
            self.add_card_to_hand(card)
        print(f"\t{self}'s hand: {self.hand}")
        return self.play(game)

    def add_card_to_hand(self, card: Card, hand_limit=HAND_LIMIT):
        if len(self.hand) < hand_limit:
            self.hand.append(card)

    def __repr__(self):
        return f"{self.name}"
