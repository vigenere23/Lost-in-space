from pydantic import BaseModel
from typing import List
from src.domain.room_allocator import RoomAllocator
from src.domain.games.game import Game
from src.domain.games.game_repository import GameRepository
from src.domain.players.player import Player
from src.domain.players.player_repository import PlayerRepository


class GameDto(BaseModel):
    id: str
    players_remaining: int

    @staticmethod
    def from_game(game: Game):
        return GameDto(id=str(game.id), players_remaining=game.players_remaining)


class GameSystem:
    def __init__(self, room_allocator: RoomAllocator, game_repository: GameRepository, player_repository: PlayerRepository):
        self.__room_allocator = room_allocator
        self.__game_repository = game_repository
        self.__player_repository = player_repository

    def list_available_games(self) -> List[GameDto]:
        available_games = self.__game_repository.find_all_available_games()
        return list(map(lambda game: GameDto.from_game(game), available_games))

    def create_game(self, host_username: str, nb_players: int, world: str):
        game = Game(host_username, nb_players, world)
        self.__game_repository.add_game(game)

    def join_game(self, host_username, **player_params):
        game = self.__find_game_by_host_username(host_username)
        player = Player(**player_params)
        game.add_player(player)

    def remove_game(self, host_username):
        game = self.__find_game_by_host_username(host_username)
        # TODO exception if game not found
        self.__games.remove(game)

    def __find_game_by_host_username(self, host_username) -> Game:
        return next((game for game in self.__games if game.get_host_username() == host_username), None)
