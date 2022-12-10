from random import shuffle
from typing import List

from marvel_snap_simulator.cards.base import Card


class Deck:
    def __init__(self, name: str, card_list: List[Card]):
        self.name = name
        self.cards = card_list
        self.current_cards = card_list.copy()
        shuffle(self.current_cards)

    def draw(self, num_of_cards=1):
        if len(self) <= 0:
            return

        if num_of_cards == 1:
            return self.get_card()

        cards = []
        while len(self) and num_of_cards:
            num_of_cards -= 1
            cards.append(self.get_card())
        return cards

    def get_card(self, index=-1):
        if len(self) <= 0:
            raise Exception("Out of cards")
        return self.current_cards.pop(index)

    def __len__(self):
        return len(self.current_cards)
