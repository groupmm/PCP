"""
Module: libpcp.numpy
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import numpy as np


def exercise_numpy_array(show_result=True):
    """Exercise 1: NumPy Array Manipulations

    Notebook: PCP_03_numpy.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    a = np.arange(10, 21, 1)
    print(a)

    a[(a <= 13) | (a > 16)] = 0
    print(a)

    b = np.append(a, np.arange(4, 7))
    print(b)

    c = np.unique(b)
    print(c)

    d = c[::-1]
    print(d, 'Type:', type(d))
    d = -np.sort(-c)
    print(d, 'Type:', type(d))
    d = np.flip(c)
    print(d, 'Type:', type(d))
    d = reversed(c)
    print(d, 'Type:', type(d))
    d = reversed(c)
    print(d, 'Type:', type(d))


def exercise_matrix_operation(show_result=True):
    """Exercise 2: Matrix Operations

    Notebook: PCP_03_numpy.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    B = np.vstack((2*np.ones((2, 4)), np.zeros((1, 4))))
    print('Matrix B: ', B, sep='\n')
    print('Shape of matrix B:', B.shape)

    D = np.array([[2, 0, 2], [-1, 5, 10], [-1, 0, 9]])
    print('Maximum of matrix D:', np.max(D))
    print('Row and column index of maximum entry:', np.unravel_index(np.argmax(D), D.shape))
    # np.argmax returns a flat index which has to be converted (e.g. using np.unravel_index)
    # to an index tuple (rows, columns)

    v = np.array([3, 2, 1])
    w = np.array([6, 5, 4])
    print('vw = ', np.dot(v, w))
    print('wv = ', np.outer(w, v), sep='\n')
    # np.multiply: element-wise multiplication, np.dot: matrix multiplication

    A = np.array([[1, 2], [3, 5]])
    v = np.array([1, 4])
    print('Inverse(A) = ', np.linalg.inv(A), sep='\n')
    print('Inverse(A)v = ', np.dot(np.linalg.inv(A), v), sep='\n')


def exercise_numpy_math_function(show_result=True):
    """Exercise 3: Mathematical NumPy Functions

    Notebook: PCP_03_numpy.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    print('\n ==== Cos and sin function ====')
    v_deg = np.array([0, 30, 45, 60, 90, 180])
    v_rad = np.deg2rad(v_deg)
    val_cos = np.cos(v_rad)
    val_sin = np.sin(v_rad)
    np.set_printoptions(formatter={'float': '{: 0.4f}'.format})
    print('deg: ', v_deg)
    print('rad: ', v_rad)
    print('cos: ', val_cos)
    print('sin: ', val_sin)

    print('\n ==== Exponential function ====')
    val_exp = np.exp(1j*v_rad)
    val_exp_real = np.real(val_exp)
    val_exp_imag = np.imag(val_exp)
    print('exp: ', val_exp)
    print('exp_real: ', val_exp_real)
    print('exp_imag: ', val_exp_imag)
    print('cos == exp_real:', np.isclose(val_cos, val_exp_real))
    print('sin == exp_imag:', np.isclose(val_sin, val_exp_imag))

    v = np.array([-3.1416, -1.5708, 0, 1.5708, 3.1416])
    print('\n ==== Rounding options ====')
    print('Original numbers:          ', v)
    print('Round to integer:          ', np.round(v))
    print('Round to three decimals:   ', np.round(v, 3))
    print('Return floor of numbers:   ', np.floor(v))
    print('Return ceil of numbers:    ', np.ceil(v))
    print('Return truncated numbers:  ', np.trunc(v))
