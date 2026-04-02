# Day 12 — Scope & Number Guessing Game

## Course Exercise

Build a number guessing game that demonstrates Python scope concepts.

> **Demo:** https://appbrewery.github.io/python-day12-demo/

### Requirements

- Generate a random number between 1 and 100
- Ask the player to choose a difficulty: `easy` (10 attempts) or `hard` (5 attempts)
- Accept guesses in a loop, telling the player "Too high" or "Too low"
- End when the player guesses correctly or exhausts their attempts

### Scope concepts covered

| Concept          | Description                                                                       |
| ---------------- | --------------------------------------------------------------------------------- |
| Global constants | `EASY_LEVEL_TURNS = 10` — ALL_CAPS, set once, never modified                      |
| `global` keyword | Modifying a global variable inside a function (and why to avoid it)               |
| Block scope      | Python has no block scope; variables in `if`/`for`/`while` live at function level |
| LEGB rule        | Local → Enclosing → Global → Built-in lookup order                                |

### ASCII art source

https://patorjk.com/software/taag/#p=display&f=Graffiti
