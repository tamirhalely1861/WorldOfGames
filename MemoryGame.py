"""Memory Game: memorise a sequence of numbers, then type it back from memory."""

import os
import random
import time

SHOW_SECONDS = 0.7
NUMBER_LOW = 1
NUMBER_HIGH = 101


def clear_screen():
    """Clear the console screen so the player cannot re-read the sequence.

    Kept local for Part 1; this reusable operation is moved to Utils.py
    in Part 2.
    """
    os.system("cls" if os.name == "nt" else "clear")


def generate_sequence(difficulty):
    """Return a list of `difficulty` random numbers between 1 and 101."""
    return [random.randint(NUMBER_LOW, NUMBER_HIGH) for _ in range(difficulty)]


def show_sequence(sequence):
    """Display the sequence briefly, then clear the screen."""
    print("Memorise this sequence:")
    print(" ".join(str(n) for n in sequence))
    time.sleep(SHOW_SECONDS)
    clear_screen()


def get_list_from_user(difficulty):
    """Return a list of exactly `difficulty` whole numbers entered by the user.

    The player types all the numbers on one line, separated by spaces. If the
    answer has the wrong length or contains a value that is not a whole number,
    the player is asked again (the original sequence is not shown again).
    """
    while True:
        raw = input(
            f"Enter the {difficulty} numbers you saw, separated by spaces: "
        ).strip()
        tokens = raw.split()
        if len(tokens) != difficulty:
            print(f"Please enter exactly {difficulty} numbers separated by spaces.")
            continue
        try:
            numbers = [int(token) for token in tokens]
        except ValueError:
            print("Please enter whole numbers only.")
            continue
        if not all(NUMBER_LOW <= n <= NUMBER_HIGH for n in numbers):
            print(f"Each number must be between {NUMBER_LOW} and {NUMBER_HIGH}.")
            continue
        return numbers


def is_list_equal(generated, guessed):
    """Return True if both lists are identical (same order and values)."""
    return generated == guessed


def play(difficulty):
    """Play a single round of Memory Game. Return True on a win."""
    sequence = generate_sequence(difficulty)
    show_sequence(sequence)
    guesses = get_list_from_user(difficulty)
    won = is_list_equal(sequence, guesses)
    if won:
        print("Correct! You remembered the whole sequence.")
    else:
        print(f"Wrong. The sequence was: {' '.join(str(n) for n in sequence)}")
    return won
