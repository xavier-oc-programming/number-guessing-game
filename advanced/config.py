from enum import Enum

# Game range
MIN_NUMBER: int = 1
MAX_NUMBER: int = 100

# Turns per difficulty
EASY_TURNS: int = 10
HARD_TURNS: int = 5

# Typewriter animation
TYPEWRITER_DELAY: float = 0.004  # seconds per character

# Display
DIVIDER_CHAR: str = "─"
DIVIDER_WIDTH: int = 52


class Difficulty(Enum):
    EASY = "easy"
    HARD = "hard"


class GuessResult(Enum):
    TOO_HIGH = "too_high"
    TOO_LOW = "too_low"
    CORRECT = "correct"
    GAME_OVER = "game_over"
