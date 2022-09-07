"""Command-line interface."""
import click

from .cards.base import Card
from .cards.cable import Cable
from .decks import Deck
from .game import Game
from .locations.gamelocations import Location
from .players import Player


@click.command()
@click.version_option()
def main() -> None:
    """Marvel Snap Simulator."""
    card_list = [
        Card("Misty Knight", 1, 2),
        Card("Angel", 1, 2),
        Card("Uatu The Watcher", 1, 2),
        Card("Quicksilver", 1, 2),
        Card("Shocker", 2, 3),
        Card("Armor", 2, 3),
        Card("Swarm", 2, 3),
        Card("Cyclops", 3, 4),
        Card("Sabretooth", 3, 4),
        Card("Thing", 4, 6),
        Card("Abomination", 5, 8),
        Card("Hulk", 6, 11),
    ]
    deck_one = Deck("Deck One", card_list)
    deck_two = Deck("Deck Two", [Cable()] * 12)
    player_one = Player("Vanilla Steve", deck_one)
    player_two = Player("Cable Man", deck_two)
    board_locations = [Location(), Location(), Location()]
    print("Starting Game")
    game = Game(player_one, player_two, board_locations)
    while not game.has_game_ended:
        game.start_turn()
    print("Game Done")


if __name__ == "__main__":
    main(prog_name="marvel-snap-simulator")  # pragma: no cover
