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
    """Créer et reçoit les arguments de la ligne de commande.

    joueur [--serveur] [--port] [--créer | --joindre | --lister] [--animer]
    [--ralentir] [--fps]

    Arguments
    ---------
    joueur: Pseudonyme du joueur.

    --serveur: adresse du serveur (python.gel.ulaval.ca)
    --port: numéro de port du serveur (31415)

    --créer (nombre_joueurs, fichier): créer une partie (1, monde2.json)
    --joindre (pseudo_hôte): joindre une partie
    --lister: lister les parties en cours

    --animer: active une animation améliorée des vaisseaux ennemis
    --ralentir: ralenti le débit des envois au serveur
    --fps: spécifie les fps
    """
    parser = argparse.ArgumentParser(
        description="Jeu 'Perdu dans l'espace!'",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("joueur",
                        help="Pseudonyme du joueur")

    parser.add_argument("--serveur", "-s",
                        metavar="adresse",
                        default="localhost",
                        help="Adresse du serveur")

    parser.add_argument("--port", "-p",
                        metavar="numéro",
                        type=int,
                        default=1234,
                        help="Numéro de port du serveur")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--créer", "-c",
                       metavar=("n", "fichier"),
                       nargs=2,
                       default=[1, "monde2.json"],
                       help="""Créer une partie de n joueurs dont la mission
                       est spécifiée dans le fichier""")

    group.add_argument("--joindre", "-j",
                       metavar="pseudo",
                       help="Pseudonyme de la partie à joindre")

    group.add_argument("--lister", "-l",
                       action="store_true",
                       help="""Affiche la liste des pseudonymes des partie
                       en attente de joueurs""")

    parser.add_argument("--animer", "-a",
                        action="store_true",
                        help="Pour un meilleur rendu des vaisseaux ennemis")

    parser.add_argument("--ralentir", "-r",
                        action="store_true",
                        help="""Envoie des requêtes moins rapidement (Si jamais
                        vous obtenez souvent cette erreur)""")

    parser.add_argument("--fps", "-f",
                        metavar="frames/s",
                        type=int,
                        default=120,
                        help="Spécifie le nombre d'images par secondes")

    parser.add_argument("--offline", "-o",
                        action="store_true",
                        help="Évite une connexion au serveur, joue solo")

    return parser.parse_args()


def parse_arguments(args):
    """Analyse les arguments reçus par la ligne de commande.

    Action par défaut: --créer (1, monde2.json)
    """
    game_params = None
    players = None
    client = None

    if len(args.joueur) > 12:
        args.joueur = "{}...".format(args.joueur[:12])
    
    if not args.offline:
        client = ClientConnection(args.joueur)
        client.connect(args.serveur, args.port)

    if args.lister:
        if not args.offline:
            print(client.lister())
        else:
            print("Impossible de contacter le serveur en mode hors-ligne.")
        return

    elif args.joindre:
        if not args.offline:
            host_pseudo = args.joindre
            print("\nEn attente de joueurs supplémentaires...")

            game = None
            try:
                print(host_pseudo)
                game = client.joindre(host_pseudo)
            except BaseException as exception:
                print("\nAucune partie hébergée par {}".format(host_pseudo))
                print(exception)
                return

            game_params, players = game["mission"], game["joueurs"]

        else:
            print("Impossible de contacter le serveur en mode hors-ligne.")            

    elif args.créer:
        player_number, filename = args.créer
        try:
            player_number = int(player_number)
            assert player_number > 0
        except ValueError:
            print("\nLe nombre de joueur doit être un nombre entier!")
            return
        except AssertionError:
            print("\nLe nombre de joueurs requis et minimum 1!")
            return

        data = None
        try:
            filepath = fh.get_path("client/mondes/{}".format(filename))
            data_file = open(filepath)
            content = data_file.read()
            data = json.loads(content)
            assert len(data) == 7

        except OSError:
            print("""\nErreur lors de la lecture du fichier...
                  \nLe fichier '{}' existe-t-il?
                  \r(Doit être placé dans le dossier 'mondes/')""".format(
                      filename
                  ))
            return

        except json.JSONDecodeError:
            print("""\nErreur lors de l'analyse du fichier...
                  \nLe fichier est-il en format JSON?""")
            return

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
            return

        except BaseException as exception:
            print("\nErreur inconnue : {}", exception)
            return

        game_params = data
        print("\nEn attente de joueurs...")

        if not args.offline:
            response = client.creer(player_number, game_params)
            print("Response:")
            if response.get("data"):
                print("received data...")
                data = response["data"]
                if data.get("players"):
                    print(data["players"])
                    start_game(client, game_params, data["players"], args)

        else:
            start_game(client, game_params, [args.joueur], args)


def start_game(client, game_params, players, args):
    """Commence la partie."""
    print("\n\nQUE LA PARTIE COMMENCE!")
    game = Game(client,
                args.joueur,
                players[0],
                players,
                *game_params,
                animate=args.animer,
                slow=args.ralentir,
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
