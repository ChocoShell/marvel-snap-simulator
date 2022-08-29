from dataclasses import dataclass
from dataclasses import field
from typing import List

from marvel_snap_simulator.cards import Card
from marvel_snap_simulator.players import Player


@dataclass
class GameLocationSide:
    player: Player
    cards: List[Card] = field(default_factory=list)
    score: int = 0

    def add(self, card: Card):
        if not self.is_full:

            first_empty_space = self.cards.index(None)

            self.cards[first_empty_space] = card

            self.calculate_score()

    @property
    def is_full(self):

        return self.empty_spaces == 0

    @property
    def empty_spaces(self):
        try:

            index = self.cards.index(None)

            return 4 - index

        except ValueError:

            return 0

    def calculate_score(self):

        """Base score calculation without effects"""

        self.score = sum(card.power for card in self.cards if card is not None)

    def __post_init__(self):
        if not self.cards:

            self.cards = self.create_cards()

    def create_cards(self):

        return [None, None, None, None]
