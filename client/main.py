import json
import pyglet as pg
import sys
import os
import common.file_helper as fh
from .src.client_connection import ClientConnection
from .src.game import Game
from .src.argparser import args


def parse_commands():
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
            response = client.list_games()

            if response.get("error"):
                print(response["error"])
                return
            elif response.get("data"):
                data = response["data"]
                print("games : {}".format(data["games"]))
            else:
                print("An unknown error has occured")

            return

        elif args.join:
            host_username = args.join
            print("\nEn attente de joueurs supplémentaires...")

            response = client.join(host_username)

            if response.get("error"):
                print(response["error"])
                return
            elif response.get("data"):
                data = response["data"]
                game_params, players = data["mission"], data["players"]
                start_game(client, game_params, players, args)
            else:
                print("An unknown error has occured")

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
        filepath = fh.get_path("client/worlds/{}.json".format(filename))
        data_file = open(filepath)
        content = data_file.read()
        data = json.loads(content)
        assert len(data) == 7
        return data

    except OSError:
        print("""\nErreur lors de la lecture du fichier...
            \nLe fichier '{}' existe-t-il?
            \r(Doit être placé dans le dossier 'worlds/')""".format(
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
    print("\n\nLet the game start!")
    game = Game(client,
                args.username,
                players[0],
                players,
                animate=args.animate,
                fps=args.fps,
                offline=args.offline,
                **game_params)
    game.start()
    pg.app.run()


if __name__ == "__main__":
    parse_commands()
