"""Shared helpers for the World of Games application."""


def get_int_in_range(prompt, low, high):
    """Prompt the user until they enter a plain base-10 integer within [low, high].

    Only strings made up of digits are accepted, so inputs like "1_0", "1.5" or
    "" are rejected rather than silently converted.
    """
    while True:
        raw = input(prompt).strip()
        if not raw.isdigit():
            print(f"Please enter a whole number between {low} and {high}.")
            continue
        try:
            value = int(raw)
        except ValueError:
            print(f"Please enter a whole number between {low} and {high}.")
            continue
        if low <= value <= high:
            return value
        print(f"Please enter a number between {low} and {high}.")
