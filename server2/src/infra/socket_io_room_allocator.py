from socketio import Server
from src.domain.room_allocator import RoomAllocator


class SocketIoRoomAllocator(RoomAllocator):

    def __init__(self, socket: Server):
        self.__socket = socket

    def join_room(self, sid, room_id: str):
        self.__socket.enter_room(sid, room_id)

    def leave_room(self, sid, room_id: str):
        self.__socket.leave_room(sid, room_id)
