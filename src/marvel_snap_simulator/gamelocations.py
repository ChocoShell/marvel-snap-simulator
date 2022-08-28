from dataclasses import dataclass
from dataclasses import field
from typing import List

from .cards import Card
from .players import Player


@dataclass
class Location:
    location_id: str = None


@dataclass
class GameLocationPlayer:
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


@dataclass
class GameLocation:
    location: Location

    players: List[GameLocationPlayer] = None
    _players: List[Player] = field(default_factory=[None, None])

    def __post_init__(self):
        self.players = [GameLocationPlayer(player) for player in self._players]

    def add(self, player, card):
        for game_player in self.players:
            if game_player.player == player:
                return game_player.add(card)
        raise Exception("Player not found")


class GameLocations:
    def __init__(self, locations: List[Location], players: List[Player]):
        self.locations = [
            GameLocation(location, _players=players) for location in locations
        ]

    def __iter__(self):
        yield from self.locations

    def __getitem__(self, item):
        return self.locations[item]
