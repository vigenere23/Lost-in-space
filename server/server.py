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

  parser.add_argument(
    "--server", "-s",
    metavar="address",
    default="0.0.0.0",
    help="Server's ip address to run on (localhost / 0.0.0.0)"
  )

  parser.add_argument(
    "--port", "-p",
    metavar="number",
    type=int,
    default="1234",
    help="Server's port number"
  )

  return parser.parse_args()


def main():
  args = init_parser()

  serversocket = ServerConnection()
  serversocket.listen(address=args.server, port=args.port)

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
