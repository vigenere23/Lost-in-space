import argparse


"""Create and receive command line arguments.

username [--server] [--port] [--create | --join | --list] [--animate]
[--slower] [--fps]

Positional arguments
--------------------
username: Player username

Named arguments
---------------
--server: server address (localhost)
--port: server port number (1234)
--animate: activated better enemies' ships animations
--fps: specify the wanted fps (120)

--offline (world): creates a solo offline game
--create (nb_players, world): create a game
--join (host_username): join a game hosted by `host_username`
--list: list waiting games
"""
__parser = argparse.ArgumentParser(
    description="Game 'Lost in space!'",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

__parser.add_argument("username",
                    help="player username")

__parser.add_argument("--server", "-s",
                    metavar="address",
                    default="localhost",
                    help="Server address")

__parser.add_argument("--port", "-p",
                    metavar="number",
                    type=int,
                    default=1234,
                    help="Server port number")

__parser.add_argument("--animate", "-a",
                    action="store_true",
                    help="Better enemies' ships animations")

__parser.add_argument("--fps", "-f",
                    metavar="frames/s",
                    type=int,
                    default=120,
                    help="Specify the wanted frame rate")

__commands_group = __parser.add_mutually_exclusive_group()
__commands_group.add_argument("--create", "-c",
                    metavar=("n", "world"),
                    nargs=2,
                    help="""Create a game of n players with a specified mission
                    stored in a json file named `world` (without extension)""")

__commands_group.add_argument("--join", "-j",
                    metavar="pseudo",
                    help="Pseudonyme de la partie à joindre")

__commands_group.add_argument("--list", "-l",
                    action="store_true",
                    help="Shows waiting games")

__commands_group.add_argument("--offline", "-o",
                    metavar="monde",
                    help="Solo offline game")

args = __parser.parse_args()
