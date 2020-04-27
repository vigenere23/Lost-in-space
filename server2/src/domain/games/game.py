from typing import List
from src.domain.id import Id
from src.domain.players.player import Player


class GameId(Id):
    def __init__(self, value: str):
        self._value = value

    @staticmethod
    def from_host_username(host_username: str):
        return GameId(host_username)


class Game:
    def __init__(self, host_username: str, nb_players: int, world: str):
        self.__id = GameId.from_host_username(host_username)
        self.__nb_players = nb_players
        self.__world = world

        self.__players: List[Player] = []
        self.__is_available = True

    @property
    def id(self) -> GameId:
        return self.__id

    @property
    def is_available(self) -> bool:
        return self.__is_available

    @property
    def players_remaining(self):
        return self.__nb_players - len(self.__players)

    def __is_full(self) -> bool:
        return len(self.__players) == self.__nb_players

    def add_player(self, player):
        self.__players.append(player)

        if self.__is_full():
            self.__is_available = False
            for player in self.__players:
                # event_emitter.send(player.sid, )
                pass

    def remove_player(self, player):
        pass
