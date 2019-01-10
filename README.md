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

**Offline**
```bash
python -m client.lost player1 -o world2
```

**List waiting games**
```bash
python -m client.lost player1 -l
```

**Host a game online (4 players)**
```bash
python -m client.lost player1 -c 4 world2
```

**Join a game online (hosted by `player1`)**
```bash
python -m client.lost player1 -j player1
```

## Creating a world

Worlds are stored as `.json` files in the `client/worlds` folder. Following is a list of possible parameters and their defaults. 

### `start_pos` (*default: [0, 0]*)

Starting position of the ships. 

### `end_pos` (*default: [100, 100]*)

Position ships must arrive to win (position of the death-star). 

### `energy` (*default: 30*)

Total energy or gas (in seconds) ships start with. 

### `accel` (*default: 100*)

Acceleration of the ships (in pixels / sec^2)

### `ang_velocity` (*default: 180*)

Angular velocity of the ships (in degrees / sec)

### `bounciness` (*default: 0.9*)

Factor of acceleration (<1 = deceleration) occured when an obstacle is hit. 

### `obstacles` (*default: []*)

List of obstacles and theirs points (in order).

Ex: 

```json
{
  // ...
  "obstacles": [
    [
      // obstacle #1
      [0, 0],       // point #1
      [0, 100],     // point #2
      [100, 100],   // point #3
      [100, 0]      // point #4
    ],
    [
      // obstacle #2
      // ...
    ]
  ]
  // ...
}
```
