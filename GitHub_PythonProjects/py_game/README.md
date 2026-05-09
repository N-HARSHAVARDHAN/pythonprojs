````md id="5c2a8f"
# Dragon Runner Game

## Aim

The aim of this project is to learn and practice game development concepts using Pygame by building a simple endless runner game.

The project focuses on understanding:

- Game loops
- Object movement
- Collision detection
- Rendering images on screen
- Score calculation
- Game over conditions

---

## Technologies Used

- Python 3
- Pygame

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````

---

## Install Pygame

```bash
pip install pygame
```

---

## Run Game

```bash
python prac1.py
```

---

## Game Features

* Endless runner gameplay
* Jump mechanics using keyboard and mouse
* Moving obstacles
* Collision detection
* Live score display
* Game over screen with final score

---

## Controls

| Action | Key         |
| ------ | ----------- |
| Jump   | SPACE       |
| Jump   | Mouse Click |

---

## Assets Used

The following assets are used in the game:

* `dragon.png`
* `player.png`
* `skyimg.jpeg`
* `ground.jpeg`

---

## Project Structure

```text
py_game/
│
├── .venv/
├── data/
│
├── dragon.png
├── player.png
├── skyimg.jpeg
├── ground.jpeg
│
├── prac1.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Concepts Practiced

* Pygame initialization
* Event handling
* Rectangles and collision detection
* Gravity and jumping physics
* Frame updates
* Animation basics
* Game state management

---

## Requirements

Generate requirements file using:

```bash
pip freeze > requirements.txt
```

```
```
