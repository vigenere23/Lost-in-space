from .src.socket_thread import SocketThread
from .src.server_connection import ServerConnection


def main():
  serversocket = ServerConnection()
  serversocket.listen()

  while True:
    s, _ = serversocket.accept()
    print("Received new connection")
    thread = SocketThread(s)
    print("Starting new thread")
    thread.start()

  serversocket.close()


if __name__ == "__main__":
  main()
