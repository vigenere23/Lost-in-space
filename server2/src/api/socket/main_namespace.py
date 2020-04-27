from socketio import AsyncNamespace
from src.api.socket.app import sio
from src.application.game_system import GameSystem


class MainNamespace(AsyncNamespace):

    def __init__(self, game_system: GameSystem):
        super().__init__('/')
        self.__game_system = game_system

    async def on_join(self, sid, data):
        self.__game_system.join_game(data['host_username'], sid, data['username'])
