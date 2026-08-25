"""
Module: libpcp.unit04
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import numpy as np


np.random.seed(0)

def add(a, b=0, c=0):
    """Function to add three numbers

    Notebook: PCP_04_control.ipynb

    Args:
        a: first number
        b: second number (Default value = 0)
        c: third number (Default value = 0)

    Returns:
        Sum of a, b and c
    """
    print('Addition: ', a, ' + ', b, ' + ', c)
    return a + b + c


def add_and_diff(a, b=0):
    """Function to add and subtract two numbers

    Notebook: PCP_04_control.ipynb

    Args:
        a: first number
        b: second number (Default value = 0)

    Returns:
        first: a + b
        second: a - b
    """
    return a + b, a - b


def sum_n(n):
    """Function that sums up the integers from 1 to n

    Notebook: PCP_04_control.ipynb

    Args:
        n: Integer number

    Returns:
        s: Sum of integers from 1 to n
    """
    s = 0
    for n in range(1, n+1):
        s = s + n
    return s


def sum_n_numpy(n):
    """Function that sums up the integers from 1 to n  using numpy

    Notebook: PCP_04_control.ipynb

    Args:
        n: Integer number

    Returns:
        s: Sum of integers from 1 to n
    """
    s = np.sum(np.arange(1, n+1))
    return s


def sum_n_math(n):
    """Function that sums up the integers from 1 to n using the idea by Gauss

    Notebook: PCP_04_control.ipynb

    Args:
        n: Integer number

    Returns:
        s: Sum of integers from 1 to n
    """
    s = n * (n + 1) // 2
    return s


def exercise_give_number(show_result=True):
    """Exercise 1: Function that provides a specified number

    Notebook: PCP_04_control.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    def give_me_a_number(s='nan'):
        """Function give_me_a_number

        Notebook: PCP_04_control.ipynb

        Args:
            s: string specifying number (Default value = 'nan')

        Returns:
            number: specified number
        """
        if s == 'large':
            number = 2 ** 100
        elif s == 'small':
            number = 2 ** (-100)
        elif s == 'random':
            number = np.random.rand()
        else:
            number = np.nan

        return number

    print('default:   ', give_me_a_number())
    print('s=\'large\': ', give_me_a_number('large'))
    print('s=\'small\': ', give_me_a_number('small'))
    print('s=\'random\':', give_me_a_number('random'))
    print('s=\'test\':  ', give_me_a_number('test'))


def exercise_row_mean(show_result=True):
    """Exercise 2: Function for Computing Row Mean

    Notebook: PCP_04_control.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    def row_mean(A):
        """Function that computes the row-wise means of A

        Notebook: PCP_04_control.ipynb

        Args:
            A: matrix

        Returns:
            row_mean: Vector containing the row-wise means
        """
        row_mean = np.zeros((A.shape[0]))

        for i in range(A.shape[1]):
            row_mean += A[:, i]

        row_mean /= A.shape[1]
        return row_mean

    A = np.array([[1, 2, 6], [5, 5, 2]])
    print('Input matrix:', A, sep='\n')
    print('Vector containing the row means: ', row_mean(A))


def exercise_odd(show_result=True):
    """Exercise 3: Function for Computing Odd-Index Vector

    Notebook: PCP_04_control.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    def vector_odd_index(x):
        """Compute Odd-Index Vector

        Notebook: PCP_04_control.ipynb

        Args:
            x: array

        Returns:
            y: output
        """
        if x.ndim > 1:
            y = None
        else:
            y = x[1::2]
        return y

    x1 = np.arange(0, 10)
    x2 = x1.reshape(1, -1)
    x3 = np.array([[1, 2, 3], [4, 5, 6]])
    print('x =', x1)
    print('y =', vector_odd_index(x1))
    print('x =', x2)
    print('y =', vector_odd_index(x2))
    print('x =', x3, sep='\n')
    print('y =', vector_odd_index(x3))


def exercise_isprime(show_result=True):
    """Exercise 4: Primality Test

    Notebook: PCP_04_control.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    def isprime(n):
        """Function that tests if number is prime

        Notebook: PCP_04_control.ipynb

        Args:
            n: Integer

        Returns:
           Boolean value
        """
        if n < 2:
            return False
        for i in range(2, n):
            remainder = np.mod(n, i)
            if remainder == 0:
                return False
        return True

    for n in [1, 17, 1221, 1223]:
        print(f'n = {n}, isprime = {isprime(n)}')

    num_max = 20
    counter = 0
    n = 1

    print(f'List of first {num_max} prime numbers:')
    while counter < num_max:
        n += 1
        result = isprime(n)
        if result is True:
            counter += 1
            print(n, end=' ')


def exercise_root(show_result=True):
    """Exercise 5: Function for Root Finding

    Notebook: PCP_04_control.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    def f(x):
        """A continuous function

        Notebook: PCP_04_control.ipynb

        Args:
            x: array or float

        Returns:
            f(x) = x**2-2
        """
        return x**2-2

    def search_root(f, a, b, thresh=10**(-5)):
        """Function that searches a root of f in a given interval [a,b] using interval halving procedure

        Notebook: PCP_04_control.ipynb

        Args:
            f: Function
            a: Interval start
            b: Interval end
            thresh: Threshold for stopping search (Default value = 10**(-5))

        Returns:
            Found root or None (in case initial condition is not fulfilled)
        """
        if a >= b:
            print(f'a = {a:.6f}, b = {b:.6f}')
            print('Interval not valid.')
            return np.nan
        elif f(a)*f(b) > 0:
            print(f'a={a:.6f}, b={b:.6f}, f(a)={f(a):.6f}, f(b)={f(b):.6f}')
            print('Sign condition not fulfilled')
            return np.nan
        else:
            while 1:
                c = (a + b) / 2
                f_c = f(c)
                f_a = f(a)
                f_b = f(b)

                print(f'a={a:.6f}, b={b:.6f}, c={c:.6f}, f(a)={f_a:.6f}, f(b)={f_b:.6f}, f(c)={f_c:.6f}')

                # check if we have already found a root
                if f_a == 0:
                    return a
                elif f_b == 0:
                    return b
                elif f_c == 0:
                    return c

                # Check sign condition and define new interval
                if f(a)*f(c) < 0:
                    b = c
                else:
                    a = c
                if b-a < thresh:
                    return c

    print('=== Function f(x) = x**2-2 ===')
    r = search_root(f, 0, 2)
    print(f'Root r = {r:.6f}, f(r) = {f(r):.6f}')
    # Root r = 1.414207, f(r) = -0.000017

    print('\n=== Function f(x) = x**2-2 ===')
    r = search_root(f, 2, 4)
    print(f'Root r = {r:.6f}, f(r) = {f(r):.6f}')

    print('\n=== Function f(x) = x**2-2 ===')
    r = search_root(f, 4, 2)
    print(f'Root r = {r:.6f}, f(r) = {f(r):.6f}')

    print('\n=== Function f(x) = sin(x) ===')
    r = search_root(np.sin, 3, 4)
    print(f'Root r = {r:.6f}, sin(r) = {np.sin(r):.6f}')
    # Root r = 3.141594, sin(r) = -0.000001
