# World of Games (WoG)

A small Python console application that bundles three playable games behind a
single menu. This is **Part 1** of a cumulative DevOps project; later parts add
persistent scores, a web service, containers, automation and deployment.

## The games

| # | Game | How it works |
|---|------|--------------|
| 1 | **Memory Game** | A sequence of random numbers (1–101) is shown for 0.7 seconds, the screen clears, and you type it back in the same order. |
| 2 | **Guess Game** | The computer picks a secret number from 1 to the difficulty, and you get one valid guess to match it. |
| 3 | **Currency Roulette** | A random amount of 1–100 USD is converted to ILS using a live exchange rate, and you estimate its value. Higher difficulty narrows the accepted range. |

Every game offers difficulty levels **1–5**: higher difficulty means a larger
range (Guess), a longer sequence (Memory), or a tighter margin of error
(Currency Roulette).

## Project structure

```
WorldOfGames/
├── MainGame.py              # Entry point: name -> welcome -> menu -> result
├── Live.py                  # Welcome message, game menu, difficulty selection
├── GuessGame.py             # Guess Game logic
├── MemoryGame.py            # Memory Game logic
├── CurrencyRouletteGame.py  # Currency Roulette logic + live USD->ILS rate
├── Utils.py                 # Shared input helper (whole number in a range)
├── requirements.txt         # External dependencies
└── README.md
```

Menu logic lives in `Live.py`; each game keeps its own rules in its own module.

## Requirements

- **Python 3.8+**
- [`requests`](https://pypi.org/project/requests/) — the only external
  dependency, used by Currency Roulette to fetch the exchange rate.

## Setup

```bash
# (optional) create and activate a virtual environment
python -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
python MainGame.py
```

You will be asked for your name, see the welcome message, choose a game (1–3)
and a difficulty (1–5), then play one round and get a win or loss result.

## Notes

- **Currency Roulette** reads the USD→ILS rate from the free, key-less
  [Frankfurter API](https://frankfurter.dev/). If the rate can't be fetched
  (no internet, timeout, bad response), the round is cancelled and never counts
  as a win. The other two games work fully offline.
- **Memory Game** clears the terminal after showing the sequence, so it's best
  run in a real terminal window rather than a limited output pane.
- Input is validated throughout: empty text, non-numbers, decimals and
  out-of-range values are rejected with a clear message and re-prompted, so bad
  input never crashes the app or starts an unintended game.
