from dataclasses import dataclass, field
from random import randint

from config import MIN_NUMBER, MAX_NUMBER, EASY_TURNS, HARD_TURNS, Difficulty, GuessResult


@dataclass
class GameState:
    difficulty: Difficulty = Difficulty.EASY
    answer: int = field(default_factory=lambda: randint(MIN_NUMBER, MAX_NUMBER))
    turns_remaining: int = EASY_TURNS
    won: bool = False
    over: bool = False

    def set_difficulty(self, difficulty: Difficulty) -> None:
        self.difficulty = difficulty
        self.turns_remaining = EASY_TURNS if difficulty == Difficulty.EASY else HARD_TURNS

    def guess(self, value: int) -> GuessResult:
        if value > self.answer:
            self.turns_remaining -= 1
            if self.turns_remaining == 0:
                self.over = True
                return GuessResult.GAME_OVER
            return GuessResult.TOO_HIGH
        elif value < self.answer:
            self.turns_remaining -= 1
            if self.turns_remaining == 0:
                self.over = True
                return GuessResult.GAME_OVER
            return GuessResult.TOO_LOW
        else:
            self.won = True
            self.over = True
            return GuessResult.CORRECT
