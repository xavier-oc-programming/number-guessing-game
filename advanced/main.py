import sys
import time

from config import Difficulty, GuessResult, MIN_NUMBER, MAX_NUMBER
from number_guessing import GameState
from display import (
    clear, divider, print_result, print_error, print_logo, get_keypress, Colors,
)

MODES: dict[str, tuple[str, Difficulty]] = {
    "1": ("Easy  — 10 turns", Difficulty.EASY),
    "2": ("Hard  —  5 turns", Difficulty.HARD),
}


def _header(title: str, subtitle: str) -> None:
    clear()
    divider()
    print(f"{Colors.CYAN}{Colors.BOLD}{title}{Colors.RESET}")
    print(f"{Colors.DIM}{subtitle}{Colors.RESET}")
    divider()


def _run_game(difficulty: Difficulty) -> None:
    state = GameState()
    state.set_difficulty(difficulty)

    _header(
        "NUMBER GUESSING",
        f"Guess a number between {MIN_NUMBER}–{MAX_NUMBER}  |  "
        f"{state.turns_remaining} turns",
    )

    while not state.over:
        print(f"{Colors.YELLOW}Turns remaining: {state.turns_remaining}{Colors.RESET}")
        raw = input("Your guess (q to quit): ").strip()
        if raw.lower() == "q":
            clear()
            sys.exit(0)
        if not raw.lstrip("-").isdigit():
            print_error("Please enter a whole number.")
            continue

        result = state.guess(int(raw))

        if result == GuessResult.CORRECT:
            print_result(f"\nCorrect! The answer was {state.answer}.")
        elif result == GuessResult.TOO_HIGH:
            print(f"{Colors.RED}Too high.{Colors.RESET}  Guess again.")
        elif result == GuessResult.TOO_LOW:
            print(f"{Colors.RED}Too low.{Colors.RESET}   Guess again.")
        elif result == GuessResult.GAME_OVER:
            print_error(f"\nOut of turns! The answer was {state.answer}.")

    print(f"\n{Colors.DIM}↑ arrow = menu   Enter = play again   q = quit{Colors.RESET}")
    while True:
        ch = get_keypress()
        if ch == "\x1b[A":       # up arrow → back to menu
            return
        elif ch in ("\r", "\n"): # Enter → replay same difficulty
            _run_game(difficulty)
            return
        elif ch == "q":
            clear()
            sys.exit(0)


def main() -> None:
    print_logo()

    while True:
        _header("NUMBER GUESSING GAME", "Select a mode — or q to quit")
        for key, (label, _) in MODES.items():
            print(f"  {Colors.YELLOW}[{key}]{Colors.RESET}  {label}")
        print(f"  {Colors.YELLOW}[q]{Colors.RESET}  Quit")

        choice = input("\nYour choice: ").strip().lower()

        if choice in MODES:
            _, difficulty = MODES[choice]
            _run_game(difficulty)
        elif choice == "q":
            clear()
            sys.exit(0)
        else:
            print_error("Invalid choice.")
            time.sleep(1)


if __name__ == "__main__":
    main()
