"""
Module: libpcp.unit04
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import numpy as np

def exercise_conditional(show_result=True):
    """Exercise 1: Conditional Number Selection.

    Notebook: PCP_04_control.ipynb

    Args:
        show_result: If True, display the results.
    """
    if not show_result:
        return

    def select_number(selection='nan'):
        """Return a number according to the supplied selection.

        Args:
            selection: String specifying the requested number.
                Default is 'nan'.

        Returns:
            Selected numerical value.
        """
        if selection == 'large':
            number = 2**100
        elif selection == 'small':
            number = 2**(-100)
        elif selection == 'random':
            number = np.random.rand()
        else:
            number = np.nan

        return number

    print('Default:   ', select_number())
    print("'large':   ", select_number('large'))
    print("'small':   ", select_number('small'))
    print("'random':  ", select_number('random'))
    print("'Large':   ", select_number('Large'))

def exercise_cumulative_sum(show_result=True):
    """Exercise 2: Computing a Cumulative Sum.

    Notebook: PCP_04_control.ipynb

    Args:
        show_result: If True, display the results.
    """
    if not show_result:
        return

    def compute_cumulative_sum(x):
        """Return the cumulative sums of a one-dimensional array.

        Args:
            x: One-dimensional NumPy array.

        Returns:
            NumPy array containing the cumulative sums.
        """
        cumulative_values = []
        running_total = 0

        for value in x:
            running_total += value
            cumulative_values.append(running_total)

        return np.array(cumulative_values)

    x = np.array([2, -1, 3, 4])

    result_loop = compute_cumulative_sum(x)
    result_numpy = np.cumsum(x)

    print('Input array:       ', x.tolist())
    print('Using a loop:      ', result_loop.tolist())
    print('Using np.cumsum(): ', result_numpy.tolist())
    print('Results agree:     ', np.array_equal(result_loop, result_numpy))

def exercise_halving(show_result=True):
    """Exercise 3: Repeated Halving.

    Notebook: PCP_04_control.ipynb

    Args:
        show_result: If True, display the results.
    """
    if not show_result:
        return

    def count_halvings(width, tolerance):
        """Return the number of halvings and the final width.

        Args:
            width: Initial positive interval width.
            tolerance: Positive upper bound for the final width.

        Returns:
            Number of halvings and final width. If either input is
            not positive, both returned values are np.nan.
        """
        if width <= 0 or tolerance <= 0:
            return np.nan, np.nan

        num_halvings = 0

        while width > tolerance:
            width /= 2
            num_halvings += 1

        return num_halvings, width

    initial_width = 1.0
    valid_tolerance = 0.01

    num_halvings, final_width = count_halvings(
        initial_width,
        valid_tolerance,
    )

    print('=== Valid input ===')
    print('Initial width:       ', initial_width)
    print('Tolerance:           ', valid_tolerance)
    print('Number of halvings:  ', num_halvings)
    print('Final width:         ', final_width)
    print('Tolerance satisfied: ', final_width <= valid_tolerance)

    invalid_tolerance = 0.0

    invalid_halvings, invalid_width = count_halvings(
        initial_width,
        invalid_tolerance,
    )

    print('\n=== Invalid input ===')
    print('Initial width:       ', initial_width)
    print('Tolerance:           ', invalid_tolerance)
    print('Number of halvings:  ', invalid_halvings)
    print('Final width:         ', invalid_width)

def exercise_isprime(show_result=True):
    """Exercise 4: Testing Prime Numbers.

    Notebook: PCP_04_control.ipynb

    Args:
        show_result: If True, display the results.
    """
    if not show_result:
        return

    def is_prime_basic(n):
        """Return True if n is prime using basic trial division."""
        if n < 2:
            return False

        for divisor in range(2, n):
            if n % divisor == 0:
                return False

        return True

    def is_prime(n):
        """Return True if n is prime using trial division up to sqrt(n)."""
        if n < 2:
            return False

        largest_divisor = int(np.sqrt(n))

        for divisor in range(2, largest_divisor + 1):
            if n % divisor == 0:
                return False

        return True

    test_numbers = [1, 17, 1221, 1223]

    print('Primality tests:')
    for n in test_numbers:
        basic_result = is_prime_basic(n)
        improved_result = is_prime(n)

        print(
            f'n = {n:4d}, '
            f'basic = {basic_result}, '
            f'improved = {improved_result}'
        )

    num_primes = 20
    prime_numbers = []
    candidate = 2

    while len(prime_numbers) < num_primes:
        if is_prime(candidate):
            prime_numbers.append(candidate)

        candidate += 1

    print(f'First {num_primes} prime numbers:')
    print(prime_numbers)

def exercise_root(show_result=True):
    """Exercise 5: Root Finding Using the Bisection Method.

    Notebook: PCP_04_control.ipynb

    Args:
        show_result: If True, display the results.
    """
    if not show_result:
        return

    def quadratic_function(x):
        """Return the value of f(x) = x**2 - 2."""
        return x**2 - 2

    def search_root(f, a, b, tolerance=1e-4, show_steps=False):
        """Approximate a root of a continuous function by bisection.

        Args:
            f: Continuous real-valued function.
            a: Left endpoint of the initial interval.
            b: Right endpoint of the initial interval.
            tolerance: Maximum width of the final interval.
                Default is 1e-4.
            show_steps: If True, display the intermediate intervals.

        Returns:
            Root approximation and number of iterations. If the input
            conditions are not satisfied, the root is np.nan.
        """
        num_iterations = 0

        if a >= b or tolerance <= 0:
            return np.nan, num_iterations

        f_a = f(a)
        f_b = f(b)

        if f_a == 0:
            return a, num_iterations

        if f_b == 0:
            return b, num_iterations

        if f_a * f_b > 0:
            return np.nan, num_iterations

        if show_steps:
            print(
                f'{"Iteration":>9} '
                f'{"a":>9} {"b":>9} {"c":>9} '
                f'{"f(a)":>10} {"f(b)":>10} {"f(c)":>10}'
            )

        while b - a > tolerance:
            c = (a + b) / 2
            f_c = f(c)
            num_iterations += 1

            if show_steps:
                print(
                    f'{num_iterations:9d} '
                    f'{a:9.6f} {b:9.6f} {c:9.6f} '
                    f'{f_a:11.6f} {f_b:11.6f} {f_c:11.6f}'
                )

            if f_c == 0:
                return c, num_iterations

            if f_a * f_c < 0:
                b = c
                f_b = f_c
            else:
                a = c
                f_a = f_c

        return (a + b) / 2, num_iterations

    print('=== Root of f(x) = x**2 - 2 on [0, 2] ===')

    root_sqrt_two, iterations = search_root(
        quadratic_function,
        0,
        2,
        show_steps=True,
    )
    reference_sqrt_two = np.sqrt(2)

    print(
        f'Approximation: r = {root_sqrt_two:.6f}, '
        f'f(r) = {quadratic_function(root_sqrt_two):.3e}'
    )
    print(
        f'Reference:     r = {reference_sqrt_two:.6f}, '
        f'f(r) = {quadratic_function(reference_sqrt_two):.3e}'
    )
    print('Iterations:   ', iterations)

    invalid_sign, _ = search_root(
        quadratic_function,
        2,
        4,
    )
    reversed_interval, _ = search_root(
        quadratic_function,
        4,
        2,
    )

    print('\n=== Invalid input intervals ===')
    print('Interval [2, 4] without a sign change:', invalid_sign)
    print('Reversed interval [4, 2]:            ', reversed_interval)

    print('\n=== Root of sin(x) on [3, 4] ===')

    root_sine, iterations = search_root(
        np.sin,
        3,
        4,
        show_steps=True,
    )

    print(
        f'Approximation: r = {root_sine:.6f}, '
        f'sin(r) = {np.sin(root_sine):.3e}'
    )
    print(
        f'Reference:     r = {np.pi:.6f}, '
        f'sin(r) = {np.sin(np.pi):.3e}'
    )
    print('Iterations:   ', iterations)
