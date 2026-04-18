# Dwarf Gold Heist

A text-based adventure game built with Python. You play as a dwarf of the Great Council, tasked with infiltrating a dragon's underground castle to recover stolen gold.

## How to Play

```
python main.py
```

Navigate the castle using directional commands:
- `north`, `south`, `east`, `west` — move between rooms
- `yes` / `no` — pick up or skip items you discover
- `exit` — quit the game

Collect all the gold before confronting the dragon. Enter the dragon's lair unprepared and your adventure ends.

## Project Structure

```
musical-octo-goggles/
├── main.py              # Game loop, movement, item handling, win/lose logic
└── game/
    ├── character.py     # Character class (name, inventory, lives)
    └── room.py          # Room class (name, exits, items, dragon flag)
```

## Requirements

- Python 3.6+
