"""
Module: libpcp.unit07
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import numpy as np
from matplotlib import pyplot as plt
from math import gcd
#from libpcp.unit06 import plot_vector


def exp_approx_Euler(x_min=0, x_max=2, x_delta=0.01, f_0=1):
    """Approximation of exponential function using Euler's method

    Notebook: PCP_07_exp.ipynb

    Args:
        x_min: Start of input interval (Default value = 0)
        x_max: End of input interval (Default value = 2)
        x_delta: Step size (Default value = 0.01)
        f_0: Initial condition (Default value = 1)

    Returns:
        f: Signal
        x: Sampled input interval
    """
    x = np.arange(x_min, x_max+x_delta, x_delta)
    N = len(x)
    f = np.zeros(N)
    f[0] = f_0
    for n in range(1, N):
        f[n] = f[n-1] + f[n-1]*x_delta
    return f, x


def plot_vector(c, color='k', start=0, linestyle='-'):
    """Plotting complex number as vector

    Notebook: PCP_07_exp.ipynb

    Args:
        c: Complex number
        color: Vector color (Default value = 'k')
        start: Start of vector (Default value = 0)
        linestyle: Line Style of vector (Default value = '-')
    """
    return plt.arrow(np.real(start), np.imag(start), np.real(c), np.imag(c),
                     linestyle=linestyle, head_width=0.05,
                     fc=color, ec=color, overhang=0.3, length_includes_head=True)


def plot_root_unity(N, ax):
    """Plotting N-th root of unity into figure with axis

    Notebook: PCP_07_exp.ipynb

    Args:
        N: Root number
        ax: Axis handle
    """
    root_unity = np.exp(2j * np.pi / N)
    root_unity_power = 1

    ax.grid()
    ax.set_xlim([-1.4, 1.4])
    ax.set_ylim([-1.4, 1.4])
    ax.set_xlabel(r'$\mathrm{Re}$')
    ax.set_ylabel(r'$\mathrm{Im}$')
    ax.set_title('Roots of unity for $N=%d$' % N)

    for n in range(0, N):
        colorPlot = 'r' if gcd(n, N) == 1 else 'k'
        plot_vector(root_unity_power, color=colorPlot)
        ax.text(np.real(1.2*root_unity_power), np.imag(1.2*root_unity_power),
                r'$\rho_{%s}^{%s}$' % (N, n), size='14',
                color=colorPlot, ha='center', va='center')
        root_unity_power *= root_unity

    circle_unit = plt.Circle((0, 0), 1, color='lightgray', fill=0)
    ax.add_artist(circle_unit)


def exercise_approx_exp(show_result=True):
    """Exercise 1: Comparing approximations of the exponential function.

    Notebook: PCP_07_exp.ipynb

    Args:
        show_result: If True, display the results.
    """
    if not show_result:
        return

    def exp_power_series(z, N):
        """Approximate exp(z) using the first N+1 series terms."""
        value = 1.0
        term = 1.0

        for n in range(1, N + 1):
            term *= z / n
            value += term

        return value

    def exp_limit_compound(z, N):
        """Approximate exp(z) using the compounding limit."""
        return (1 + z / N)**N

    # Test several real and complex inputs
    for z in [1, -1, 1j * np.pi, 1 + 1j]:
        exact = np.exp(z)
        print(f'\nz = {z}, np.exp(z) = {exact:.8f}')

        for N in [10, 100]:
            series = exp_power_series(z, N)
            compound = exp_limit_compound(z, N)
            print(
                f'N = {N:3d}: series = {series:.8f}, '
                f'compound = {compound:.8f}'
            )

    # Compare the approximation errors
    z = 1 + 1j
    N_values = np.arange(1, 26)
    exact = np.exp(z)

    error_series = np.array([
        abs(exp_power_series(z, N) - exact) for N in N_values
    ])
    error_compound = np.array([
        abs(exp_limit_compound(z, N) - exact) for N in N_values
    ])

    # Avoid zero values on the logarithmic axis
    precision = np.finfo(float).eps
    error_series = np.maximum(error_series, precision)
    error_compound = np.maximum(error_compound, precision)

    plots = [
        ('linear', 'Linear Scale'),
        ('log', 'Logarithmic Scale'),
    ]

    fig, axes = plt.subplots(
        1, 2, figsize=(6.2, 2.2), layout='tight'
    )

    for ax, (scale, title) in zip(axes, plots):
        ax.plot(N_values, error_series, 'ro-', markersize=3,
                label='Power series')
        ax.plot(N_values, error_compound, 'ko-', markersize=3,
                label='Compounding limit')
        ax.set_yscale(scale)
        ax.set_xlim(1, 25)
        ax.set_xticks([1, 5, 10, 15, 20, 25])
        ax.set_title(title)
        ax.set_xlabel('$N$')
        ax.set_ylabel('Absolute error')
        ax.grid(which='both', alpha=0.3)

    axes[0].legend();
    plt.show()
    print(
        '\nFor sufficiently large N, a displayed error may stop decreasing because'
        '\nfloating-point precision has been reached. Such a plateau reflects a'
        '\nlimitation of the numerical computation rather than a failure of the'
        '\nunderlying mathematical approximation.'        
    )    
    

def exercise_gaussian(show_result=True):
    """Exercise 2: Exploring the Gaussian function.

    Notebook: PCP_07_exp.ipynb

    Args:
        show_result: If True, display the resulting figure.
    """
    if not show_result:
        return

    def compute_gaussian_1D(x, mu=0, sigma=1):
        """Evaluate a Gaussian function pointwise.

        Args:
            x: NumPy array of input values.
            mu: Mean.
            sigma: Standard deviation.

        Returns:
            Gaussian function values.
        """
        return (
            np.exp(-0.5 * ((x - mu) / sigma)**2)
            / (sigma * np.sqrt(2 * np.pi))
        )

    x = np.linspace(-5, 5, 1001)
    colors = ['blue', 'black', 'red']

    fig, axes = plt.subplots(
        1, 2, figsize=(6.2, 2.3), layout='tight', sharey=True
    )

    # Compare different centers
    for mu, color in zip([-2, 0, 2], colors):
        axes[0].plot(
            x, compute_gaussian_1D(x, mu=mu, sigma=1),
            color=color, label=rf'$\mu={mu},\ \sigma=1$',
        )

    # Compare different widths
    for sigma, color in zip([0.5, 1, 2], colors):
        axes[1].plot(
            x, compute_gaussian_1D(x, mu=-1, sigma=sigma),
            color=color, label=rf'$\mu=-1,\ \sigma={sigma}$',
        )

    for ax, title in zip(
        axes, ['Varying the Mean', 'Varying the Standard Deviation']
    ):
        ax.set_xlim(-5, 5)
        ax.set_xlabel('$x$')
        ax.set_title(title)
        ax.grid(alpha=0.3)
        ax.legend()

    axes[0].set_ylabel('$g(x)$');


def exercise_spiral(show_result=True):
    """Exercise 3: Generating complex spirals.

    Notebook: PCP_07_exp.ipynb

    Args:
        show_result: If True, display the resulting figure.
    """
    if not show_result:
        return

    def generate_spiral(rad_start=0.5, rad_end=2, num_rot=3,
                        angle_start=0, N=151):
        """Generate a spiral represented by complex numbers."""
        rotations = np.linspace(0, num_rot, N)
        radius = np.linspace(rad_start, rad_end, N)
        angle = 2 * np.pi * rotations + np.deg2rad(angle_start)
        return radius * np.exp(1j * angle)

    def plot_spiral(ax, spiral, rad_end, title):
        """Plot a complex spiral."""
        limit = 1.1 * rad_end
        ax.plot(spiral.real, spiral.imag)
        ax.set(
            xlim=(-limit, limit), ylim=(-limit, limit),
            xlabel=r'$\operatorname{Re}$',
            ylabel=r'$\operatorname{Im}$',
            title=title, aspect='equal',
        )
        ax.grid(alpha=0.3)

    examples = [
        (0.2, 1.0, 2, 0, 101),
        (0.2, 1.5, 3.25, 180, 201),
        (0.5, 2.0, 6, 90, 301),
    ]

    fig, axes = plt.subplots(
        1, 3, figsize=(6.2, 2.4), layout='tight'
    )

    for ax, parameters in zip(axes, examples):
        rad_start, rad_end, num_rot, angle_start, N = parameters
        spiral = generate_spiral(*parameters)
        title = (
            f'{num_rot} rotations, start {angle_start}°\n'
            rf'$r:{rad_start}\rightarrow{rad_end}$'
        )
        plot_spiral(ax, spiral, rad_end, title)

def exercise_spiral2(show_result=True):
    """Exercise 3: Spiral Generation

    Notebook: PCP_07_exp.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    def generate_spiral(rad_start=0.5, rad_end=2, num_rot=5, angle_start=0, N=201):
        """Generate spiral

        Notebook: PCP_07_exp.ipynb

        Args:
            rad_start: Radius to start with (Default value = 0.5)
            rad_end: Radius to stop with  (Default value = 2)
            num_rot: Number of rotations (Default value = 5)
            angle_start: Angle to start with in degrees (Default value = 0)
            N: Number of data points to represent the spiral (Default value = 201)

        Returns:
            spiral: Spiral
        """
        gamma = np.linspace(0, num_rot, N)
        rad = rad_start + (gamma/num_rot) * (rad_end - rad_start)
        spiral = np.exp(2*np.pi*1j*gamma) * rad
        angle_start_rad = np.deg2rad(angle_start)
        spiral = np.exp(1j*angle_start_rad) * spiral
        return spiral

    def plot_spiral(ax, spiral, rad_end):
        """Plot spiral

        Notebook: PCP_07_exp.ipynb

        Args:
            ax: Axis handle
            spiral: Spiral
            rad_end: Radius to stop with (maximal radius)
        """
        ax.set_xlim([-rad_end*1.1, rad_end*1.1])
        ax.set_ylim([-rad_end*1.1, rad_end*1.1])
        ax.plot(spiral.real, spiral.imag)
        ax.grid()
        ax.set_aspect('equal')

    plt.figure(figsize=(6.2, 3))
    ax = plt.subplot(1, 3, 1)
    [rad_start, rad_end, num_rot, angle_start, N] = [0.2, 2, 10, 0, 501]
    spiral = generate_spiral(rad_start, rad_end, num_rot, angle_start, N)
    plot_spiral(ax, spiral, rad_end)

    ax = plt.subplot(1, 3, 2)
    [rad_start, rad_end, num_rot, angle_start, N] = [0.5, 1, 3.75, 90, 501]
    spiral = generate_spiral(rad_start, rad_end, num_rot, angle_start, N)
    plot_spiral(ax, spiral, rad_end)

    ax = plt.subplot(1, 3, 3)
    [rad_start, rad_end, num_rot, angle_start, N] = [0.01, 10, 20, 0, 1001]
    spiral = generate_spiral(rad_start, rad_end, num_rot, angle_start, N)
    plot_spiral(ax, spiral, rad_end)

    plt.tight_layout()
