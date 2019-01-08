class Game:
  def __init__(self, host, nb_players, mission):
    self.host = host
    self.nb_players = nb_players
    self.mission = mission
    self.players = [] # Player

  def get_players(self):
    return [player.username for player in self.players]

  def is_full(self):
    return len(self.players) == self.nb_players

  def get_statuses(self):
    statuses = {}
    for player in self.players:
      statuses[player.username] = player.status

    return statuses
