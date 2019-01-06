from common.socket_connection import SocketConnection, ERROR, DATA

class ServerConnection(SocketConnection):
  def __init__(self):
    super().__init__()

  
  def listen(self, address="0.0.0.0", port=1234):
    self._socket.bind((address, port))
    self._socket.listen(5)
    message = "Listening at {} on port {}"
    self.print_message(message)


  def accept(self):
    s, address = self._socket.accept()
    socket = ServerConnection()
    socket.set_socket(s)
    return (socket, address)


  def send_error(self, message):
    response = {
      "type": ERROR,
      "message": message
    }
    self.send(response)


  def send_data(self, data):
    response = {
      "type": DATA,
      "data": data
    }
    self.send(response)
