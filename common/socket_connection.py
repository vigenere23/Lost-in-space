import socket
import struct
import json
import sys
import threading
from enum import Enum


class ResponseType(Enum):
  DATA = 1,
  ERROR = 2


class SocketConnection:
  def __init__(self):
    self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


  def set_socket(self, s):
    self.__socket = s


  def listen(self, address="0.0.0.0", port=1234):
    self.__socket.bind((address, port))
    self.__socket.listen(5)
    message = "Listening at {} on port {}"
    self.print_message(message)


  def connect(self, address="0.0.0.0", port=1234):
    self.__socket.connect((address, port))
    message = "Connected to {} on port {}"
    self.print_message(message)


  def accept(self):
    s, address = self.__socket.accept()
    client_socket = SocketConnection()
    client_socket.set_socket(s)
    return (client_socket, address)


  def close(self):
    self.__socket.close()


  def print_message(self, message):
    formatted_msg = message.format(self.__socket.getsockname()[0], self.__socket.getsockname()[1])
    print()
    print(formatted_msg)


  def send(self, data):
    if isinstance(data, str):
      data = data.encode()
    elif isinstance(data, dict):
      data = json.dumps(data).encode()
  
    self.__socket.sendall(struct.pack('!I', len(data)))
    self.__socket.sendall(data)


  def __recvall(self, count):
    buf = b""
    while count > 0:
      recv_size = 0
      if count >= 4096:
        recv_size = 4096
        count -= 4096
      else:
        recv_size = count
        count = 0

      newbuf = self.__socket.recv(recv_size)
      if not newbuf: return None
      buf += newbuf
      count -= len(newbuf)
    return buf


  def recv(self):
    try:
      length, = struct.unpack('!I', self.__recvall(4))
      return self.__recvall(length).decode()
    except Exception:
      return None


  def recv_obj(self):
    data = self.recv()
    try:
      return json.loads(data)
    except Exception:
      return None
