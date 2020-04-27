from typing import Dict
from src.domain.players.player import Player, PlayerId
from src.domain.players.player_repository import PlayerRepository


class InMemoryPlayerRepository(PlayerRepository):

    def __init__(self):
        self.__players: Dict[PlayerId, Player] = {}

    def find_player_by_id(self, player_id: PlayerId) -> Player:
        return self.__players[player_id]
