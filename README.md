# Day 12 — Number Guessing Game

**100 Days of Code · The Complete Python Pro Bootcamp**

A terminal number guessing game built in two versions: a minimal procedural
script close to the original course solution, and a fully rebuilt OOP version
with a structured display layer, typed enums, and a navigable menu.

---

## Table of Contents

- [Game Overview](#game-overview)
- [How to Run](#how-to-run)
- [Controls](#controls)
- [Project Structure](#project-structure)
- [Architecture — Advanced Version](#architecture--advanced-version)
- [Module Reference](#module-reference)
- [Day 12 Concepts](#day-12-concepts)

---

## Game Overview

The computer picks a random number between **1 and 100**. You choose a
difficulty, then guess the number. After each guess the game tells you whether
you were too high or too low. You win by guessing correctly before your turns
run out.

| Difficulty | Turns |
| ---------- | ----- |
| Easy       | 10    |
| Hard       | 5     |

The optimal strategy (binary search — always guess the midpoint) solves any
game in at most **7 guesses**, so Hard mode is beatable with perfect play.

---

## How to Run

**Requirements:** Python 3.10+, standard library only — no `pip install` needed.

```bash
# Version selector (recommended entry point)
python menu.py

# Run a specific version directly
python original/main.py
python advanced/main.py
```

---

## Controls

| Input                 | Effect                                 |
| --------------------- | -------------------------------------- |
| A number + Enter      | Submit a guess                         |
| `q` + Enter           | Quit immediately (works at any prompt) |
| Enter (end of game)   | Play again with the same difficulty    |
| ↑ arrow (end of game) | Return to the mode selection menu      |

---

## Project Structure

```
Day 12/
├── menu.py                  # Entry point — clears screen, shows logo,
│                            # launches original/ or advanced/ via subprocess
├── requirements.txt         # Standard library only
├── docs/
│   └── COURSE_NOTES.md      # Original exercise brief + scope concepts table
│
├── original/                # Course version — procedural, single file
│   ├── main.py              # All game logic in one file, close to course solution
│   └── art.py               # ASCII logo
│
└── advanced/                # Rebuilt version — modular OOP
    ├── main.py              # Orchestration only: collect input → call logic → call display
    ├── number_guessing.py   # Pure game logic — GameState dataclass, no UI imports
    ├── display.py           # All terminal output: colors, typewriter, dividers, keypresses
    └── config.py            # Constants and enums only
```

---

## Architecture — Advanced Version

The advanced version enforces a strict separation of concerns across three layers:

```
┌─────────────────────────────────────────────────────┐
│  main.py  — orchestration                           │
│  Collects input → calls logic → calls display       │
├─────────────────────────────────────────────────────┤
│  number_guessing.py  — logic layer                  │
│  Zero UI imports. Pure state and rules.             │
├─────────────────────────────────────────────────────┤
│  display.py  — presentation layer                   │
│  Owns every print(), color, animation, keypress.    │
├─────────────────────────────────────────────────────┤
│  config.py  — constants + enums                     │
│  Imported by all layers. No logic, no output.       │
└─────────────────────────────────────────────────────┘
```

**Key rule:** `number_guessing.py` never imports from `display.py` or `main.py`.
This means the game logic can be tested, reused, or extended without touching
any UI code.

**Data flow for one guess:**

```
user types a number
    → main.py validates input (is it a digit? is it "q"?)
    → GameState.guess(value) → returns GuessResult enum
    → main.py reads the result and calls the appropriate display function
```

---

## Module Reference

### `config.py`

Holds every constant and multi-state flag used across the project.

| Name               | Type    | Value                                         | Purpose                                 |
| ------------------ | ------- | --------------------------------------------- | --------------------------------------- |
| `MIN_NUMBER`       | `int`   | `1`                                           | Lower bound of the guessing range       |
| `MAX_NUMBER`       | `int`   | `100`                                         | Upper bound of the guessing range       |
| `EASY_TURNS`       | `int`   | `10`                                          | Turns allowed on Easy difficulty        |
| `HARD_TURNS`       | `int`   | `5`                                           | Turns allowed on Hard difficulty        |
| `TYPEWRITER_DELAY` | `float` | `0.004`                                       | Seconds per character in logo animation |
| `DIVIDER_CHAR`     | `str`   | `─`                                           | Character used to draw horizontal rules |
| `DIVIDER_WIDTH`    | `int`   | `52`                                          | Width of horizontal rules in characters |
| `Difficulty`       | `Enum`  | `EASY`, `HARD`                                | Difficulty level flag                   |
| `GuessResult`      | `Enum`  | `TOO_HIGH`, `TOO_LOW`, `CORRECT`, `GAME_OVER` | Outcome of a single guess               |

---

### `number_guessing.py`

Contains `GameState` — a dataclass that owns all game state and rules.
No `print()` calls, no imports from `display` or `main`.

```python
@dataclass
class GameState:
    difficulty: Difficulty          # current difficulty
    answer: int                     # randomly generated on construction
    turns_remaining: int            # decremented on each wrong guess
    won: bool                       # True when the correct number is guessed
    over: bool                      # True when won or turns_remaining hits 0
```

**Methods:**

`set_difficulty(difficulty: Difficulty) → None`
Sets `turns_remaining` to `EASY_TURNS` or `HARD_TURNS` based on the chosen
difficulty. Called once after construction before the game loop starts.

`guess(value: int) → GuessResult`
The core game rule. Compares `value` against `answer`:

- If wrong: decrements `turns_remaining`. If it hits 0, sets `over = True`
  and returns `GuessResult.GAME_OVER`.
- If correct: sets `won = True` and `over = True`, returns `GuessResult.CORRECT`.
- Otherwise returns `GuessResult.TOO_HIGH` or `GuessResult.TOO_LOW`.

The caller (`main.py`) reads the returned enum and decides what to display.
`GameState` never decides what the user sees.

---

### `display.py`

Owns all terminal output. Nothing else in the project calls `print()` directly
except through this module.

| Name                      | Description                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| `LOGO`                    | Multi-line ASCII art string for "GUESS THE NUMBER"                                            |
| `Colors`                  | Class of ANSI escape code constants: `CYAN`, `GREEN`, `RED`, `YELLOW`, `DIM`, `BOLD`, `RESET` |
| `clear()`                 | Clears the terminal (`cls` on Windows, `clear` on Unix)                                       |
| `typewriter(text, delay)` | Prints text character by character with a configurable delay                                  |
| `divider()`               | Prints a full-width horizontal rule in DIM color                                              |
| `print_result(message)`   | Prints a message in GREEN (win / positive outcome)                                            |
| `print_error(message)`    | Prints a message in RED (loss / invalid input)                                                |
| `get_keypress()`          | Reads a single raw keypress without requiring Enter (uses `tty`/`termios`)                    |
| `print_logo()`            | Clears screen, animates the logo with `typewriter()`, pauses briefly                          |

**Color conventions:**

| Color       | Used for                           |
| ----------- | ---------------------------------- |
| CYAN + BOLD | Section headers                    |
| GREEN       | Correct guess, positive feedback   |
| RED         | Wrong direction, errors, game over |
| YELLOW      | Key values (turns remaining)       |
| DIM         | Instructions, hints, dividers      |

---

### `main.py` (advanced)

Orchestrates the game. Contains no game rules and no raw `print()` calls —
only input collection, logic calls, and display calls.

`MODES` dict maps keystrokes to `(label, Difficulty)` pairs, making it trivial
to add new modes without touching game or display code.

`_header(title, subtitle)` — clears screen and prints a consistent
`divider → CYAN header → DIM subtitle → divider` block used at the start of
every screen.

`_run_game(difficulty)` — main game loop. Runs until `state.over` is True,
then waits for a keypress: Enter replays, ↑ returns to menu, `q` exits.

---

## Day 12 Concepts

This project was built as part of a lesson on **Python scope and namespaces**.

### The LEGB Rule

Python resolves names by searching four scopes in order:

| Scope         | Description                           | Example                                                  |
| ------------- | ------------------------------------- | -------------------------------------------------------- |
| **L**ocal     | Inside the current function           | A variable declared inside `guess()`                     |
| **E**nclosing | Outer function (for nested functions) | A variable in an outer function accessed by an inner one |
| **G**lobal    | Module-level                          | `EASY_TURNS = 10` at the top of a file                   |
| **B**uilt-in  | Python's built-in names               | `len`, `range`, `print`                                  |

### Global Constants vs. the `global` Keyword

The course contrasts two patterns:

```python
# Bad — relies on the global keyword to mutate shared state
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1

# Good — pass data in, return data out, no shared mutation
def increase_enemies(enemy_count):
    return enemy_count + 1

enemies = increase_enemies(enemies)
```

In the game, `EASY_TURNS` and `HARD_TURNS` are global **constants** (ALL_CAPS
convention) — they are set once and never modified. The `global` keyword is
never used.

### Block Scope

Unlike JavaScript, C, or Java, Python does **not** create a new scope for
`if`, `for`, or `while` blocks. A variable declared inside an `if` block is
accessible outside it, as long as you're in the same function.

```python
def example():
    if True:
        x = 10
    print(x)  # works fine — x is function-scoped, not block-scoped
```
