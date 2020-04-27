from typing import List
from fastapi.responses import HTMLResponse
from fastapi_utils.api_model import APIModel
from src.application.game_system import GameSystem, GameDto
from src.api.rest.base_controller import BaseController


class CreateGameRequest(APIModel):
    host_username: str
    nb_players: int
    world: str


class MainController(BaseController):
    def __init__(self, game_system: GameSystem):
        super().__init__()
        self.__game_system = game_system

    async def list_games(self) -> str:
        game_dtos = self.__game_system.list_available_games()
        return game_dtos

    async def create_game(self, request: CreateGameRequest):
        self.__game_system.create_game(request.host_username, request.nb_players, request.world)
        return HTMLResponse(status_code=200)

    def _register_routes(self):
        self._get('/list', self.list_games, response_model=List[GameDto])
        self._post('/create', self.create_game)
