"""
Module: libpcp.unit03
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import numpy as np


def exercise_numpy_array(show_result=True):
    """Exercise 1: NumPy Array Manipulations.

    Notebook: PCP_03_numpy.ipynb

    Args:
        show_result: If True, display the intermediate results.
    """
    if not show_result:
        return

    # Create the initial array
    a = np.arange(10, 21)
    print('Initial array a:', a)

    # Replace values outside the interval [14, 16] with zero
    mask = (a <= 13) | (a > 16)
    a[mask] = 0
    print('Modified array a:', a)

    # Append the values 4, 5, and 6
    b = np.append(a, np.arange(4, 7))
    print('Extended array b:', b)

    # Remove duplicates and sort them in ascending order
    c = np.unique(b)
    print('Unique values c:', c)

    # Approach 1: Reverse using slicing
    d = c[::-1]
    print('Using slicing:', d)

    # Approach 2: Sort and then reverse
    d = np.sort(c)[::-1]
    print('Using np.sort():', d)

    # Approach 3: Reverse using np.flip()
    d = np.flip(c)
    print('Using np.flip():', d)

def exercise_matrix_operation(show_result=True):
    """Exercise 2: Matrix Operations.

    Notebook: PCP_03_numpy.ipynb

    Args:
        show_result: If True, display the intermediate results.
    """
    if not show_result:
        return

    # Construct the vectors and matrix A
    u = np.array([[1, 2]])
    w = np.array([[3, 5]])
    v = np.array([[1], [4]])
    A = np.vstack((u, w))

    print(f'Row vector u: {u.tolist()}, shape: {u.shape}')
    print(f'Row vector w: {w.tolist()}, shape: {w.shape}')
    print(f'Column vector v: {v.tolist()}, shape: {v.shape}')
    print(f'Matrix A: {A.tolist()}, shape: {A.shape}')

    # Locate the maximum entry
    maximum = np.max(A)
    flat_index = np.argmax(A)
    row_index, column_index = np.unravel_index(flat_index, A.shape)

    print('Maximum entry of A:', maximum)
    print('Flat index of maximum:', flat_index)
    print('Row and column indices:',
          (int(row_index), int(column_index)))

    # Compare the products uv and vu
    product_uv = np.dot(u, v)
    product_vu = np.dot(v, u)

    print(f'Product uv: {product_uv.tolist()}, '
          f'shape: {product_uv.shape}')
    print(f'Product vu: {product_vu.tolist()}, '
          f'shape: {product_vu.shape}')

    # Compare element-wise and matrix multiplication
    elementwise_product = np.multiply(A, A)
    matrix_product = np.dot(A, A)

    print('Element-wise product of A with A:',
          elementwise_product.tolist())
    print('Matrix product of A with A:',
          matrix_product.tolist())

    # Invert A and solve Ax = v
    inverse_A = np.linalg.inv(A)
    x = np.dot(inverse_A, v)
    verification = np.dot(A, x)

    print('Inverse of A:', inverse_A.round(10).tolist())
    print('Solution x = inverse(A)v:', x.round(10).tolist())
    print('Verification Ax:', verification.round(10).tolist())
    print('Original vector v:', v.tolist())

def exercise_numpy_math_function(show_result=True):
    """Exercise 3: Trigonometric Functions and Complex Exponentials.

    Notebook: PCP_03_numpy.ipynb

    Args:
        show_result: If True, display the intermediate results.
    """
    if not show_result:
        return

    # Control the display of floating-point values
    np.set_printoptions(
        precision=4,
        suppress=True,
        formatter={'float': '{: 0.4f}'.format}
    )

    # Convert angles from degrees to radians
    v_deg = np.array([0, 30, 45, 60, 90, 180])
    v_rad = np.deg2rad(v_deg)

    print('Angle conversion')
    print('Angles in degrees:             ', v_deg)
    print('Angles in radians:             ', v_rad)

    # Evaluate sine and cosine
    cos_values = np.cos(v_rad)
    sin_values = np.sin(v_rad)

    print('\nTrigonometric functions')
    print('Cosine values:                 ', cos_values)
    print('Sine values:                   ', sin_values)
    print('sin(30 degrees):               ', sin_values[1])
    print('cos(60 degrees):               ', cos_values[3])
    print('sin(90 degrees):               ', sin_values[4])
    print('cos(180 degrees):              ', cos_values[5])

    # Evaluate the complex exponential
    z = np.exp(1j * v_rad)
    real_z = np.real(z)
    imaginary_z = np.imag(z)

    print('\nComplex exponential exp(1j * v_rad):')
    print(z, sep='\n')
    print('Real parts:                    ', real_z)
    print('Imaginary parts:               ', imaginary_z)

    # Verify Euler's formula
    print('Real parts match cosine:       ',
          np.isclose(real_z, cos_values))
    print('Imaginary parts match sine:    ',
          np.isclose(imaginary_z, sin_values))
    