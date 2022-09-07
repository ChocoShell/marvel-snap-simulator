from typing import List

from marvel_snap_simulator.players import Player

from .gamelocations import GameLocation
from .gamelocations import Location


class Board:
    # This class is a mess
    def __init__(self, locations: List[Location], players: List[Player]):
        self.locations = [
            GameLocation(location, _players=players) for location in locations
        ]

    def __iter__(self):
        yield from self.locations

    def __getitem__(self, item):
        return self.locations[item]
