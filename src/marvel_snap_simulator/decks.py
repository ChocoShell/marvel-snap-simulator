from random import shuffle


class Deck:
    def __init__(self, name, card_list):
        self.name = name
        self.cards = card_list
        self.current_cards = card_list.copy()
        shuffle(self.current_cards)

    def draw(self, num_of_cards=1):
        return [self._draw() for _ in range(num_of_cards)]

    def _draw(self):
        # print(f"Cards left: {len(self.current_cards)}")
        return self.current_cards.pop()
