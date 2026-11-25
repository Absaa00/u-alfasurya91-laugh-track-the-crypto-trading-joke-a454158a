#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Prints a single original one-line joke about crypto and trading life
to stdout. The line stays under the 200-character cap, is fully
deterministic, and needs no network access or third-party packages.
"""

JOKE = "I bought the dip so many times my exchange sent me a loyalty card: buy ten dips, get the eleventh crash free."


def main():
    assert len(JOKE) < 200, "joke must stay under the 200-character cap"
    assert JOKE.count("\n") == 0, "entry must be a single line"
    print(JOKE)


if __name__ == "__main__":
    main()
