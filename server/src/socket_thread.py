import threading
import src.game_system as gs


class SocketThread(threading.Thread):
  def __init__(self, s):
    super()
    self.socket = s

  def run(self):
    while True:
      data = self.socket.recv()

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
        self.create(command)
      elif command == "join":
        self.join(command)
      elif command == "list":
        self.list_games(command)

    self.socket.close()

  def create(self, command):
    if not command.get("host"):
      self.socket.send_error("A host must be specified")
    elif not command.get("nb_players"):
      self.socket.send_error("The numbers of players is required")
    elif not command.get("mission"):
      self.socket.send_error("A mission file is required")
    
    print("Creating new game hosted by '{}'".format(command["host"]))
    gs.new_game(self.socket, command["host"], command["nb_players"], command["mission"])

  def join(self, command):
    pass

  def list_games(self, command):
    pass