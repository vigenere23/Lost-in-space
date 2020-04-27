class GameNotFoundException(Exception):

    def __init__(self, host_username: str):
        super().__init__("No game hosted by {} was found.".format(host_username))
        self.host_username = host_username
