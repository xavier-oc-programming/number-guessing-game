# Day 12 — Number Guessing Game

100 Days of Code · The Complete Python Pro Bootcamp

## What it does

Guess a randomly chosen number between 1 and 100. Choose easy (10 turns) or hard (5 turns); the game tells you whether each guess is too high or too low.

## How to run

```bash
python menu.py          # version selector
python original/main.py # course version directly
python advanced/main.py # OOP version directly
```

## Structure

```
Day 12/
├── menu.py                  # version selector (subprocess launcher)
├── requirements.txt         # standard library only
├── docs/
│   └── COURSE_NOTES.md      # original exercise + scope concepts
├── original/
│   ├── main.py              # procedural, close to course solution
│   └── art.py               # ASCII logo
└── advanced/
    ├── main.py              # menu loop + MODES dispatcher
    ├── number_guessing.py   # pure logic — GameState dataclass
    ├── display.py           # all terminal UI (Colors, typewriter, etc.)
    └── config.py            # constants + Difficulty / GuessResult enums
```

## Key concepts (Day 12)

- Global constants vs. the `global` keyword
- Python's LEGB scope rule (Local → Enclosing → Global → Built-in)
- Block scope: Python doesn't have it
