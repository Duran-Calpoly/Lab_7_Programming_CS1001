"""CS 1001 - Lab Programming 7: Input, Output, and File Processing.

ONE DAY: Wednesday, November 18, 2026. November 16 is a quiz day.

Complete only the three TODO functions in this file. Do not change their
signatures or the provided main driver. This lab assumes all numeric text
is valid and all named input files exist (error handling is Lab 8).

Tests: python -m unittest test_1.py
Manual keyboard demo: python day1.py
Manual file demo:     python day1.py pairs.txt results.txt
"""


def sum_pair(text: str) -> float:
    """Return the sum of two numbers encoded in a string.

    The numbers are separated by whitespace. Use split() and float().
    Examples:
        sum_pair("3 4") -> 7.0
        sum_pair("  -2.5   7  ") -> 4.5

    Do not read input, print, or open files in this helper function.
    """
    # TODO (Task 1): Split, convert to floats, add, and return the total.
    raise NotImplementedError


def keyboard_sum() -> None:
    """Prompt for one pair of numbers and print their sum.

    Prompt exactly: Enter two numbers: 
    If the user types "3 4", print exactly: Sum: 7.0
    Reuse sum_pair(). Return None.
    """
    # TODO (Task 2): Call input() once, reuse sum_pair(), and print result.
    raise NotImplementedError


def sum_file(input_filename: str, output_filename: str) -> None:
    """Read number pairs from one file and write one sum per output line.

    Each input line contains two valid numbers (e.g., "3.0 4.0\n").
    Use with open(..., 'r') and with open(..., 'w').
    Reuse sum_pair(line) for each input line; do not repeat parsing.
    Write str(total) followed by '\n' for every line.
    An empty input file creates an empty output file. Return None.
    """
    # TODO (Task 3): Read lines, call sum_pair(), and write results.
    raise NotImplementedError


if __name__ == "__main__":
    # This driver is PROVIDED. Read it, but do not change it.
    # sys.argv[0] is the script name; remaining items are arguments.
    import sys

    if len(sys.argv) == 1:
        keyboard_sum()
    elif len(sys.argv) == 3:
        sum_file(sys.argv[1], sys.argv[2])
        print(f"Saved results to {sys.argv[2]}")
    else:
        print("Usage: python day1.py [input_filename output_filename]")
