# Lost in space

This project was made as a school project for the course GLO-1901 : Introduction to programmation using Python. The goal is to control a small spaceship and reach the end (identified by a Death-Star) the fastest possible (if against others), within the given amount of gas. This solo or multiplier game (up to 4 players) will guarantee a combination of stress, excitement and lots of fun!

## How to start

First, clone the project and install python along with the pyglet library. Then, go to the project's root folder and : 

### Start the server

```bash
python -m server.server
```

### Play the game

**Offline :**
```bash
python -m client.perdu player1 -o world2
```

**List waiting games:**
```bash
python -m client.perdu player1 -l
```

**Host a game online (4 players) [IN DEVELOPMENT] :**:
```bash
python -m client.perdu player1 -c 4 world2
```

**Join a game online (hosted by player1) [IN DEVELOPMENT] :**
```bash
python -m client.perdu player1 -j player1
```

**PS.:** All the worlds (e.g. `world2`) must be in a correct json format and stored in the `client/worlds/` folder.
