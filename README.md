# Text-Based RPG Game Engine

This project is a work-in-progress Python engine for building a text-based RPG games. It is designed around modular components for characters, items, gear, actions, and game logic, with all game data stored in CSV files for easy editing and extension. I built this to practice using Classes and OOP.

## Author: Sapna Mehta-Gertz

## Current Features
- Items, gear, and enemies are loaded from 'base' CSV files at runtime. Data is created for testing purposes only now, and will likely change.
- Three types of characters can be created, and additional types can be built from existing Classes
- Some functions allow for interactive creation, equipping, using, and dropping of new items and gear.
- Gear and abilities are tied to character jobs (e.g., Ninja, Thief, Wizard).

## Current Status
This project is under active development and not yet playable. Many features are incomplete or only partially implemented. Contributions and suggestions are welcome!

## Key Files
- `project.py`: Will be the main script; currently being built to test how modules interact
- `game_engine.py`: Data loading and writing logic
- `character.py`, `items.py`, `gear.py`: Core game object definitions
- `actions.py`: Character actions (undeveloped)
- CSV files: Game data (`items.csv`, `gear.csv`, `enemies_list.csv`, `enemy_base.csv`)

## Getting Started
1. Clone the repository.
2. Review the code and CSV files to understand the current structure.
3. Run `project.py` to see example item and gear generation.
4. Extend or modify gameplay by editing the Python modules and CSVs.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
