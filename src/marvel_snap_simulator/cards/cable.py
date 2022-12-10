from .base import OnRevealCard


class Cable(OnRevealCard):
    name = "Cable"
    cost = 2
    power = 2
    effect = "On Reveal: Put the bottom card of your opponent's deck into your hand."

    def on_reveal(self, player, game):
        # Find opponent
        opponent = game.get_player(player, get_opponent=True)
        me = game.get_player(player)
        # Find opponent's deck
        if len(opponent.deck) > 0:
            # Get bottom card
            stolen_card = opponent.deck.get_card(0)
            # Steal card
            me.add_card_to_hand(stolen_card)
