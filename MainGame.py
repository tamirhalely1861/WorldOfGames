"""Entry point for the World of Games application."""

from Live import welcome, load_game


def main():
    name = input("Please enter your name: ").strip() or "Player"
    print(welcome(name))
    result = load_game()
    if result is True:
        print("\nWell done! You won this round.")
    elif result is False:
        print("\nBetter luck next time!")
    # result is None: the round was cancelled; load_game already explained why.


if __name__ == "__main__":
    main()
