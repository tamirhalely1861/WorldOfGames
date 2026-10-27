"""Guess Game: guess the secret number between 1 and the chosen difficulty."""

import random

from Utils import get_int_in_range


def generate_number(difficulty):
    """Return a random whole number between 1 and difficulty (inclusive).

    The result is the secret number; it is not printed here so it stays
    hidden until the player has made a guess.
    """
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    """Ask the user to guess a number between 1 and difficulty."""
    return get_int_in_range(
        f"Guess a number between 1 and {difficulty}: ", 1, difficulty
    )


def compare_results(secret_number, guess):
    """Return True if the guess matches the secret number."""
    return secret_number == guess


def play(difficulty):
    """Play a single round of Guess Game. Return True on a win."""
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    won = compare_results(secret_number, guess)
    if won:
        print("Correct! You guessed the number.")
    else:
        print(f"Wrong. The number was {secret_number}.")
    return won
