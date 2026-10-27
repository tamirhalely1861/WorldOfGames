"""Currency Roulette: estimate the ILS value of a random USD amount.

During normal play the USD->ILS rate is fetched from a live currency API.
The rate fetch and the interval calculation are kept in separate functions so
the calculation can be checked with controlled values.
"""

import random
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

import requests

MIN_USD = 1
MAX_USD = 100

# Free, key-less exchange-rate endpoint.
API_URL = "https://api.frankfurter.app/latest?from=USD&to=ILS"
API_TIMEOUT_SECONDS = 10

# Monetary values are kept to two decimal places.
CENTS = Decimal("0.01")


class RateUnavailableError(Exception):
    """Raised when the USD->ILS exchange rate cannot be retrieved."""


def get_usd_to_ils_rate():
    """Return the current USD -> ILS exchange rate from a live currency API.

    Raises RateUnavailableError if the API is unreachable, times out, returns
    an invalid response, or does not include the ILS rate.
    """
    try:
        response = requests.get(API_URL, timeout=API_TIMEOUT_SECONDS)
        response.raise_for_status()
        data = response.json()
        return data["rates"]["ILS"]
    except (requests.RequestException, ValueError, KeyError) as error:
        raise RateUnavailableError(str(error)) from error


def to_money(value):
    """Return `value` as a Decimal rounded to two decimal places."""
    return Decimal(str(value)).quantize(CENTS, rounding=ROUND_HALF_UP)


def get_money_interval(difficulty, correct_value):
    """Return the (lower, upper) bounds of accepted answers for the round.

    `difficulty` is d and `correct_value` is t (the correct ILS amount):
        lower = t - (5 - d)
        upper = t + (5 - d)
    Both endpoints count as valid answers.
    """
    margin = 5 - difficulty
    lower = correct_value - margin
    upper = correct_value + margin
    return lower, upper


def get_guess_from_user(usd_amount):
    """Ask for a non-negative decimal ILS guess, re-prompting if invalid."""
    while True:
        raw = input(f"How many ILS are {usd_amount} USD worth? ").strip()
        try:
            guess = Decimal(raw)
        except InvalidOperation:
            print("Please enter a non-negative number.")
            continue
        if not guess.is_finite() or guess < 0:
            print("Please enter a non-negative number.")
            continue
        return guess


def play(difficulty):
    """Play a single round of Currency Roulette. Return True on a win.

    Raises RateUnavailableError if the exchange rate cannot be retrieved, so the
    caller can cancel the round rather than treating it as a loss.
    """
    usd_amount = random.randint(MIN_USD, MAX_USD)
    rate = get_usd_to_ils_rate()
    correct_value = to_money(usd_amount * Decimal(str(rate)))
    lower, upper = get_money_interval(difficulty, correct_value)

    guess = get_guess_from_user(usd_amount)

    won = lower <= guess <= upper
    if won:
        print(f"Correct! {usd_amount} USD is {correct_value} ILS.")
    else:
        print(
            f"Wrong. {usd_amount} USD is {correct_value} ILS "
            f"(accepted range was {lower} to {upper})."
        )
    return won
