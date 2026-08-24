"""
Module: libpcp.unit10
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

string = 'This is a test string'
string_init = 'This is a test string specified in the __init__.py file'
a, b, c = 1, 2, 3


def add(a, b=0, c=0):
    """Function to add three numbers

    Notebook: PCP_10_module.ipynb

    Args:
        a: first number
        b: second number (Default value = 0)
        c: third number (Default value = 0)

    Returns:
        Sum of a, b and c
    """
    d = a + b + c
    print('Addition: ', a, ' + ', b, ' + ', c, ' = ', d)
    return d


def test_function_init(string_input = string_init):
    """Test function specified in the __init__.py file

    Notebook: PCP_10_module.ipynb

    Args:
        string_input: Input string (Default value = string_init)
    """
    print('=== Test:', string_input, '===')
