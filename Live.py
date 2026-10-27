"""Welcome message, game selection and difficulty selection for World of Games."""

import GuessGame
import MemoryGame
import CurrencyRouletteGame
from CurrencyRouletteGame import RateUnavailableError
from Utils import get_int_in_range

GAMES = {
    1: (
        "Memory Game",
        MemoryGame,
        "recall a sequence of numbers shown for 0.7 seconds",
    ),
    2: (
        "Guess Game",
        GuessGame,
        "match the computer's secret number",
    ),
    3: (
        "Currency Roulette",
        CurrencyRouletteGame,
        "estimate the ILS value of a randomly selected USD amount",
    ),
}

MIN_DIFFICULTY = 1
MAX_DIFFICULTY = 5


def welcome(name):
    """Return a welcome message greeting the player by name."""
    return (
        f"Hello {name} and welcome to the World of Games (WoG).\n"
        "Here you can find many cool games to play."
    )


def choose_game():
    """Show the game menu and return the chosen (title, module)."""
    print("Please choose a game to play:")
    for number, (title, _module, description) in GAMES.items():
        print(f"{number}. {title} - {description}")
    choice = get_int_in_range(
        "Enter your choice: ", min(GAMES), max(GAMES)
    )
    title, module, _description = GAMES[choice]
    return title, module


def choose_difficulty():
    """Prompt for and return a difficulty level between 1 and 5."""
    return get_int_in_range(
        f"Please choose game difficulty "
        f"from {MIN_DIFFICULTY} to {MAX_DIFFICULTY}: ",
        MIN_DIFFICULTY,
        MAX_DIFFICULTY,
    )


def load_game():
    """Run the full selection flow and play one round of the chosen game.

    Returns True for a win and False for a loss. Returns None when the round
    was cancelled (for example, the exchange rate could not be retrieved, or a
    technical error occurred) so a cancelled round is never reported as a win
    or a loss.
    """
    title, module = choose_game()
    difficulty = choose_difficulty()
    print(f"\nStarting {title} (difficulty {difficulty})...\n")
    try:
        return bool(module.play(difficulty))
    except RateUnavailableError as error:
        print(
            "Round cancelled: could not retrieve the exchange rate "
            f"({error})."
        )
        return None
    except Exception as error:
        print(f"Round cancelled because of a technical error: {error}")
        return None
