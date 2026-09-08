"""
Module: libpcp.unit10
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT License, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks:
https://www.audiolabs-erlangen.de/PCP
"""

DEFAULT_MESSAGE = 'Hello from libpcp.unit10.'


def add(a, b):
    """Return the sum of two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of a and b.
    """
    return a + b


def print_message(message=DEFAULT_MESSAGE):
    """Print a message.

    Args:
        message: Message to print (default: DEFAULT_MESSAGE).
    """
    print(message)