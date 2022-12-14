from .plays import Play


class DumbAIMixin:
    """
    This is my first attempt at an "AI"

    It will find the most expensive, playable card in hand and
        play it at a location you are losing or tied at.
    """

    def play(self, game):
        energy = game.turn
        current_energy = energy
        play_card = None
        play_location = None
        is_player_one = game.players[0] == self
        location_score_index = 0 if is_player_one else 1

        plays = []
        while current_energy > 0:
            play_card = None
            play_location = None
            for ind, card in enumerate(self.hand):
                if card.cost <= current_energy:
                    current_energy -= card.cost
                    self.hand.pop(ind)
                    play_card = card
                    break
            for i, location in enumerate(game.locations):
                if not location.sides[location_score_index].is_full:
                    me = location.sides[location_score_index].score
                    opp = location.sides[(location_score_index + 1) % 2].score
                    if me <= opp:
                        play_location = i
                        break
            if play_card is not None and play_location is not None:
                plays += [Play(i, play_card)]
            else:
                current_energy -= 1
        return plays
