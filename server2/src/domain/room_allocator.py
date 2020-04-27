from abc import ABC, abstractmethod


class RoomAllocator(ABC):

    @abstractmethod
    def join_room(self, sid, room: str):
        pass

    @abstractmethod
    def leave_room(self, sid, room: str):
        pass
