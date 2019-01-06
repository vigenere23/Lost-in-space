import socket
import struct
import json
import sys
import threading
from enum import Enum


DATA = 200
ERROR = 500


class SocketConnection:
  def __init__(self):
    self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


  def set_socket(self, s):
    self._socket = s


  def close(self):
    self._socket.close()


  def print_message(self, message):
    formatted_msg = message.format(self._socket.getsockname()[0], self._socket.getsockname()[1])
    print()
    print(formatted_msg)


  def send(self, data):
    if isinstance(data, str):
      data = data.encode()
    elif isinstance(data, dict):
      data = json.dumps(data).encode()
  
    self._socket.sendall(struct.pack('!I', len(data)))
    self._socket.sendall(data)


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

      newbuf = self._socket.recv(recv_size)
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
