from src.socket_connection import SocketConnection
from src.socket_thread import SocketThread


def main():
  serversocket = SocketConnection()
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
