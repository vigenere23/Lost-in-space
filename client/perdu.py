#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Fichier principal."""

import json
import argparse
import pyglet as pg
import sys
import os

import common.file_helper as fh
from .scripts.client_connection import ClientConnection
from .scripts.game import Game


def init_parser():
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
    parser = argparse.ArgumentParser(
        description="Jeu 'Perdu dans l'espace!'",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("username",
                        help="player username")

    parser.add_argument("--server", "-s",
                        metavar="address",
                        default="localhost",
                        help="Server address")

    parser.add_argument("--port", "-p",
                        metavar="number",
                        type=int,
                        default=1234,
                        help="Server port number")

    parser.add_argument("--animate", "-a",
                        action="store_true",
                        help="Better enemies' ships animations")

    parser.add_argument("--fps", "-f",
                        metavar="frames/s",
                        type=int,
                        default=120,
                        help="Specify the wanted frame rate")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--create", "-c",
                       metavar=("n", "world"),
                       nargs=2,
                       help="""Create a game of n players with a specified mission
                       stored in a json file named `world` (without extension)""")

    group.add_argument("--join", "-j",
                       metavar="pseudo",
                       help="Pseudonyme de la partie à joindre")

    group.add_argument("--list", "-l",
                       action="store_true",
                       help="Shows waiting games")

    group.add_argument("--offline", "-o",
                        metavar="monde",
                        help="Solo offline game")

    return parser.parse_args()


def parse_arguments(args):
    """Analyse les arguments reçus par la ligne de commande.

    Action par défaut: --créer (1, monde2)
    """

    if len(args.username) > 12:
        args.username = "{}...".format(args.username[:12])
    
    if args.offline:
        world = args.offline
        try:
            game_params = get_world(world)
        except Exception as e:
            print(e)
            return

        start_game(None, game_params, [args.username], args)

    else:
        client = ClientConnection(args.username)
        client.connect(args.server, args.port)

        if args.list:
            print(client.list_games())
            return

        elif args.join:
            host_username = args.join
            print("\nEn attente de joueurs supplémentaires...")

            game = None
            try:
                print(host_username)
                game = client.join(host_username)
            except BaseException as exception:
                print("\nAucune partie hébergée par {}".format(host_username))
                print(exception)
                return

            game_params, players = game["mission"], game["players"]
            start_game(client, game_params, players, args)

        elif args.create:
            player_number, world = args.create
            try:
                player_number = int(player_number)
                assert player_number > 0
            except ValueError:
                print("\nLe nombre de joueur doit être un nombre entier!")
                return
            except AssertionError:
                print("\nLe nombre de joueurs requis et minimum 1!")
                return
            
            try:
                game_params = get_world(world)
            except Exception as e:
                print(e)
                return

            print("\nEn attente de joueurs...")

            response = client.create(player_number, game_params)
            print("Response:")
            if response.get("error"):
                print("Erreur lors de la création de la partie.")
                print(response["error"])
                return
            elif response.get("data"):
                data = response["data"]
                if data.get("players"):
                    start_game(client, game_params, data["players"], args)
            else:
                print("Erreur inconnue")
                return

def get_world(filename):
    try:
        filepath = fh.get_path("client/mondes/{}.json".format(filename))
        data_file = open(filepath)
        content = data_file.read()
        data = json.loads(content)
        assert len(data) == 7
        return data

    except OSError:
        print("""\nErreur lors de la lecture du fichier...
            \nLe fichier '{}' existe-t-il?
            \r(Doit être placé dans le dossier 'mondes/')""".format(
                filename
            ))
        return None

    except json.JSONDecodeError:
        print("""\nErreur lors de l'analyse du fichier...
            \nLe fichier est-il en format JSON?""")
        return None

    except AssertionError:
        print("""\nLe fichier ne contient pas l'information nécessaire...
            \nLe fichier doit être de la forme suivante:
            \n\rposition de départ: list (coord 2D)
            \rposition d'arrivée: list (coord 2D)
            \rliste des sommets des obstacles: list of lists of lists
            \raccélération: float (pixels/s^2)
            \rénergie: float (secondes)
            \rvitesse de rotation: float (°/s)
            \rcoefficient de rebond: float (%)""")
        return None

    except BaseException as exception:
        print("\nErreur inconnue : {}", exception)
        return None


def start_game(client, game_params, players, args):
    """Commence la partie."""
    print("\n\nQUE LA PARTIE COMMENCE!")
    game = Game(client,
                args.username,
                players[0],
                players,
                *game_params,
                animate=args.animate,
                fps=args.fps,
                offline=args.offline)
    game.start()
    pg.app.run()


def main():
    """Fonction principale."""

    args = init_parser()
    parse_arguments(args)


if __name__ == "__main__":
    main()
