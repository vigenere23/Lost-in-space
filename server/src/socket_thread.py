import threading
from . import game_system as gs


class SocketThread(threading.Thread):
  def __init__(self, s):
    super().__init__()
    self.socket = s

  def run(self):
    while True:
      data = self.socket.recv_obj()

      if not data:
        # remove user from game
        # if host send error data?
        break
      if not data.get("command"):
        break

      print("received data : {}".format(data))
      command = data["command"]

      print("Received command '{}'".format(command))

      if command == "create":
        self.create(data)
      elif command == "join":
        self.join(data)
      elif command == "list":
        self.list_games(data)

    self.socket.close()

  def create(self, data):
    if not data.get("host"):
      self.socket.send_error("A host must be specified")
    elif not data.get("nb_players"):
      self.socket.send_error("The numbers of players is required")
    elif not data.get("mission"):
      self.socket.send_error("A mission file is required")
    
    print("Creating new game hosted by '{}'".format(data["host"]))
    gs.new_game(self.socket, data["host"], data["nb_players"], data["mission"])

  def join(self, data):
    pass

  def list_games(self, data):
    pass
