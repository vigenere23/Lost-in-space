import socketio
from src.api.socket.app import sio
from src.api.socket.main_namespace import MainNamespace
from src.api.rest.app import app
from src.api.rest.main_controller import MainController
from src.application.game_system import GameSystem
from src.infra.socket_io_room_allocator import SocketIoRoomAllocator
from src.infra.repositories.in_memory_player_repository import InMemoryPlayerRepository
from src.infra.repositories.in_memory_game_repository import InMemoryGameRepository


player_repository = InMemoryPlayerRepository()
game_repository = InMemoryGameRepository()
room_allocator = SocketIoRoomAllocator(sio)
game_system = GameSystem(room_allocator, game_repository, player_repository)
main_controller = MainController(game_system)

sio.register_namespace(MainNamespace(game_system))
app.include_router(main_controller.router)

socket_api = socketio.ASGIApp(sio)
app.mount('/socket', socket_api)
