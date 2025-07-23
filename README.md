# Minimal Fighter

A small two-player fighting game built with Pygame. Each player controls a
colored rectangle and can move left/right, jump, and attack. When a player's
health reaches zero, the opponent wins.

## Controls

- **Player 1 (Red)**
  - Move left: `A`
  - Move right: `D`
  - Jump: `W`
  - Attack: `Space`

- **Player 2 (Blue)**
  - Move left: `Left Arrow`
  - Move right: `Right Arrow`
  - Jump: `Up Arrow`
  - Attack: `Enter`

## Installation

Install Python 3 and install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Game

```bash
python3 game.py
```

The game runs in a window. Use the controls above to fight. When one player's
health bar is depleted, a winner message appears.

