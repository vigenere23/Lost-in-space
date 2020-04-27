from typing import List, Dict
from src.domain.games.game import Game, GameId
from src.domain.games.game_repository import GameRepository


class InMemoryGameRepository(GameRepository):

    def __init__(self):
        self.__games: Dict[GameId, Game] = {}

    def find_all_available_games(self) -> List[Game]:
        return list(filter(
            lambda game: game.is_available,
            self.__games.values()
        ))

    def find_game_by_id(self, game_id: GameId) -> Game:
        return self.__games[game_id]

    def add_game(self, game: Game):
        self.__games[game.id] = game

    def remove_game(self, game_id: GameId):
        del self.__games[game_id]
