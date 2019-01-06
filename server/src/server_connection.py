from common.socket_connection import SocketConnection, ResponseType

class ServerConnection(SocketConnection):
  def __init__(self):
    super().__init__()


  def send_error(self, message):
    response = {
      "type": ResponseType.ERROR,
      "message": message
    }
    self.send(response)


  def send_data(self, data):
    response = {
      "type": ResponseType.DATA,
      "data": data
    }
    self.send(response)
