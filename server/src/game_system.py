from .game import Game
from .player import Player


_games = {} # host_username: Game
_players = {} # socket : Player


def new_game(socket, host, nb_players, mission):
  if _games.get(host):
    socket.send_error("The host '{}' already has a game".format(host))
    return

  game = Game(host, nb_players, mission)
  _games[host] = game

  add_player(socket, host, host)


def add_player(socket, host, username):
  if not _games.get(host):
    socket.send_error("The host '{}' does not host a game".format(host))
    return

  game = _games[host]
  player = Player(username, socket, game)

  _players[socket] = player
  game.players.append(player)

  if game.is_full():
    player_list = game.get_players()
    data = {
      "players": player_list,
      "mission": game.mission
    }
    for player in game.players:
      player.socket.send_data(data)


def update_status(socket, status):
  player = _players[socket]
  player.status = status

  game = player.game
  statuses = game.get_statuses()
  data = {
    "statuses": statuses
  }
  socket.send_data(data)