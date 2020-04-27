class PlayerId:
    id: str

    @staticmethod
    def from_sid(sid):
        return PlayerId(id=str(sid))


class Player:

    def __init__(self, sid, username: str, game):
        self.__id = PlayerId.from_sid(sid)
        self.__username = username
        self.__game = game

    @property
    def id(self) -> PlayerId:
        return self.__id

    @property
    def username(self) -> str:
        return self.__username

    @property
    def game(self):
        return self.__game
