"""One Letter: Coffee or Tea.

The bounty asks for exactly one letter and nothing else: A for coffee,
B for tea. This entry answers A.

Why coffee: it is the first decision of the day, made before words are
available. Tea waits politely; coffee is already poured, dark, hot, and
gone before the kettle has even boiled. The letter is the whole answer,
so the program prints it with no extra output.
"""

import sys


def choose() -> str:
    """Return the single letter for this entry: A, coffee."""
    return "A"


def main() -> None:
    sys.stdout.write(choose())


if __name__ == "__main__":
    main()
