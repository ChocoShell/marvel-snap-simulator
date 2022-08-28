from random import choice
from typing import List

from .gamelocations import GameLocations
from .gamelocations import Location
from .players import Player
from .plays import Play


class Game:
    def __init__(
        self, player_one: Player, player_two: Player, board_locations: List[Location]
    ):
        # Whats in a game?
        self.players = [player_one, player_two]
        for player in self.players:
            player.draw_starting_hand()

        self.player_initiative = self.players[0]

        self.locations = GameLocations(board_locations, self.players)
        self.turn = 0

    def start_turn(self):
        self.turn += 1
        print(f"Turn {self.turn}:")

        all_plays = [player.take_turn(self) for player in self.players]

        for player, plays in zip(self.players, all_plays):
            self.play(player, plays)

        winning_player = self.get_winning_player()
        if self.has_game_ended:
            return self.get_game_outcome(winning_player)
        else:
            self.player_initiative = winning_player

    def play(self, player: Player, plays: List[Play]):
        player_index = 0 if player == self.players[0] else 1
        for play in plays:
            if play.card.cost <= self.turn:
                self.locations[play.location].players[player_index].add(play.card)
                print(
                    f"\t{player.name} plays {play.card.name}"
                    f" at location {play.location+1}"
                )
            else:
                print(
                    f"\tERROR: {player.name} tried to play {play.card.name}"
                    f" at location {play.location+1}"
                )

    def get_winning_player(self):
        total = 0
        p1_total = 0
        p2_total = 0
        for location in self.locations:
            p1_score = location.players[0].score
            p2_score = location.players[1].score
            if p1_score > p2_score:
                total += 1
            elif p1_score < p2_score:
                total -= 1
            p1_total += p1_score
            p2_total += p2_score

        if total == 0 and p1_total > p2_total or total > 0:
            return self.players[0]
        elif total == 0 and p1_total < p2_total or total < 0:
            return self.players[1]
        else:
            return choice(self.players) if self.has_game_ended else None  # noqa: S311

    def get_game_outcome(self, player):
        if player is not None:
            print(f"Player {player.name} won!")
        else:
            print("It was a draw...")

    @property
    def has_game_ended(self):
        return self.turn >= 6