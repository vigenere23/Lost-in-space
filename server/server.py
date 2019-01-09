from .src.socket_thread import SocketThread
from .src.server_connection import ServerConnection
import argparse


def init_parser():
  parser = argparse.ArgumentParser(
    description="Server of game 'Lost in space!'",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )

  parser.add_argument(
    "--verbose", "-v",
    action="store_true",
    help="Show some logs"
  )

  return parser.parse_args()


def main():
  args = init_parser()

  serversocket = ServerConnection()
  serversocket.listen()

  while True:
    s, _ = serversocket.accept()
    
    if args.verbose:
      print("Received new connection")
    
    thread = SocketThread(s, args)
    
    if args.verbose:
      print("Starting new thread")
    
    thread.start()

  serversocket.close()


if __name__ == "__main__":
  main()
