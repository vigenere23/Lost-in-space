from abc import ABC, abstractmethod
from src.domain.players.player import Player, PlayerId


class PlayerRepository(ABC):

    @abstractmethod
    def find_player_by_id(self, player_id: PlayerId) -> Player:
        pass
