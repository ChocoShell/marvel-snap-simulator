from typing import Optional


class Card:
    def __init__(self, name: str, cost: int, power: int, effect: Optional[str] = None):
        self.name = name
        self.cost = cost
        self.power = power
        self.effect = effect

    def play(self, *args, **kwargs):
        pass

    def __repr__(self):
        return f"{self.name} <{self.cost}> [{self.power}]"


class OnRevealCard(Card):
    def __init__(self):
        super().__init__(self.name, self.cost, self.power, self.effect)

    def play(self, player, game):
        self.on_reveal(player, game)
        super().play()

    def on_reveal(self):
        """
        Affects the game in some way.
        Could affect the board, the players, the decks, scores, other locations, etc.
        """
