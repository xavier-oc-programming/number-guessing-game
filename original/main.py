from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    """Check guess against answer. Returns remaining turns, or None on correct."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")


def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Please type 'easy' or 'hard'.")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"\nYou have {turns} attempts remaining.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns is None:
            return
        if turns == 0:
            print(f"You've run out of guesses. The answer was {answer}.")
            return
        print("Guess again.")


game()
