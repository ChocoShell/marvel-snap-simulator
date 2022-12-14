from dataclasses import dataclass
from dataclasses import field
from typing import List

from marvel_snap_simulator.players import Player

from .exceptions import PlayerNotFoundError
from .players import GameLocationSide


@dataclass
class Location:
    location_id: str = None


@dataclass
class GameLocation:
    location: Location
    sides: List[GameLocationSide] = None
    _players: List[Player] = field(default_factory=[None, None])

    def __post_init__(self):
        self.sides = [GameLocationSide(player) for player in self._players]

    def add(self, player, card):
        for game_player in self.sides:
            if game_player.player == player:
                return game_player.add(card)
        raise PlayerNotFoundError("Player not found")
