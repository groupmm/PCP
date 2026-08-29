"""
Module: libpcp.unit02
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import copy


def exercise_list(show_result=True):
    """Exercise 1: Basic List Manipulations

    Notebook: PCP_02_python.ipynb

    Args:
        show_result: Show the sample solution if True.
    """
    if not show_result:
        return

    student_list = [
        [123, 'Meier', 'Max'],
        [456, 'Smith', 'Sam']
    ]
    print('Initial:', student_list)

    student_list.append([789, 'Wang', 'Wei'])
    print('Extended:', student_list)

    print('Reversed:', student_list[::-1])
    print('First name of second student:', student_list[1][2])
    print('Number of students:', len(student_list))

    student_list_copy = copy.deepcopy(student_list)
    del student_list_copy[:2]
    student_list_copy[0][0] = 777

    print('Modified copy:', student_list_copy)
    print('Original:', student_list)
    print('Original ID remains unchanged:', student_list[-1][0] == 789)


def exercise_dict(show_result=True):
    """Exercise 2: Basic Dictionary Manipulations

    Notebook: PCP_02_python.ipynb

    Args:
        show_result: Show the sample solution if True.
    """
    if not show_result:
        return

    student_dict = {
        123: ['Meier', 'Max'],
        456: ['Smith', 'Sam']
    }
    print('Initial:', student_dict)

    student_dict[789] = ['Wang', 'Wei']
    print('Extended:', student_dict)

    print('Student IDs:', list(student_dict.keys()))
    print('Student names:', list(student_dict.values()))
    print('Last name for ID 456:', student_dict[456][0])

    del student_dict[456]
    print('After deleting ID 456:', student_dict)

    print('Number of remaining students:', len(student_dict))