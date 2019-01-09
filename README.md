# Lost in space

This project was made as a school project for the course GLO-1901 : Introduction to programmation using Python. The goal is to control a small spaceship and reach the end (identified by a Death-Star) the fastest possible (if against others), within the given amount of gas. This solo or multiplier game (up to 4 players) will guarantee a combination of stress, excitement and lots of fun!

## Installation

```bash
git clone https://github.com/vigenere23/lost-in-space.git
cd lost-in-space
pip install -r requirements.txt
```

## Basic commands

See `--help` for a comprehensive list of all the commands.

All worlds (e.g. `world2`) must be in a correct json format and stored in the `client/worlds/` folder.

### Starting the server

```bash
python -m server.server
```

### Playing the game

**Offline :**
```bash
python -m client.lost player1 -o world2
```

**List waiting games :**
```bash
python -m client.lost player1 -l
```

**Host a game online (4 players) :**
```bash
python -m client.lost player1 -c 4 world2
```

**Join a game online (hosted by player1) :**
```bash
python -m client.lost player1 -j player1
```
