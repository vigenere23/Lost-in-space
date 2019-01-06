class Game:
  def __init__(self, host, nb_players, mission):
    self.host = host
    self.nb_players = nb_players
    self.mission = mission
    self.players = [] # Player

  def get_players(self):
    return [player.username for player in self.players]

  def is_full(self):
    print(len(self.players))
    print(self.nb_players)
    return len(self.players) == self.nb_players
