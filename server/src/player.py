class Player:
  def __init__(self, username, socket, game=None):
    self.username = username
    self.socket = socket
    self.game = game # Game
    self.status = ()
