from common.socket_connection import SocketConnection

class ClientConnection(SocketConnection):
  def __init__(self, username):
    super().__init__()
    self.username = username


  def connect(self, address="0.0.0.0", port=1234):
    self._socket.connect((address, port))
    message = "Connected to {} on port {}"
    self.print_message(message)

  
  def create(self, nombre_joueurs, mission):
    """Communique avec le serveur de jeu pour créer une partie.

    :param n: nombre de joueurs désirés (min: 1)
    :param mission: tuple des paramètres de la mission.

    :returns: un dictionnaire contenant une clé 'joueurs' à laquelle
    est associée un tuple de pseudonymes de joueur.
    """
    request = {
        "command": "create",
        "host": self.username,
        "nb_players": nombre_joueurs,
        "mission": mission
    }

    self.send(request)
    return self.recv_obj()


  def list_games(self):
    """Demande au serveur la liste des parties en attente de joueurs.

    :returns: dictionnaire contenant où les clés sont les pseudonymes des
    créateurs des parties en attente et les valeurs le nombre de places
    disponibles.
    """
    request = {"command": "list"}

    self.send(request)
    return self.recv_obj()


  def join(self, hote):
    """Indique au serveur que l'on désire joindre la partie crée par hote.

    :param hote: pseudonyme de l'hôte de la partie à joindre.

    :returns: dictionnaire contenant les clés:
        - 'joueurs' : la liste de noms de joueurs membres de la partie;
        - 'mission' : tuple des paramètres de la mission.
    """
    request = {"command": "join",
                "host": hote,
                "username": self.username}

    self.send(request)
    return self.recv_obj()


  def report(self, status):
    """Rapporte au serveur l'état de notre vaisseau.

    :param status : tuple of status ((pos_x, pos_y), (vel_x, vel_y), rot_degrees)

    :returns: dictionnaire contenant les clés:
        - 'gagnant': pseudonyme du gagnant si la partie est terminée;
          `None` autrement;
        - '<pseudo1>': dernier état connu du vaisseau du joueur <pseudo1>;
        - ...
    La fonction peut aussi retourner None si aucune réponse n'a été obtenue
    à temps du serveur de jeu.
    """
    request = {
        "command": "update",
        "status": status
    }

    self.send(request)
    return self.recv_obj()
