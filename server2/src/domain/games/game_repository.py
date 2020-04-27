from abc import ABC, abstractmethod
from typing import List
from src.domain.games.game import Game, GameId


class GameRepository(ABC):

    @abstractmethod
    def find_all_available_games(self) -> List[Game]:
        pass

    @abstractmethod
    def find_game_by_id(self, game_id: GameId) -> Game:
        pass

    @abstractmethod
    def add_game(self, game: Game):
        pass

    @abstractmethod
    def remove_game(self, game_id: GameId):
        pass
