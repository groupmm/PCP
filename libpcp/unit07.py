"""
Module: libpcp.unit07
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import numpy as np
from matplotlib import pyplot as plt
from math import gcd
from libpcp.unit06 import plot_vector


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
    """Exercise 1: Approximation of Exponential Function via Power Series

    Notebook: PCP_07_exp.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    def exp_power_series(z, N):
        """Compute power series for exponential function

        Notebook: PCP_07_exp.ipynb

        Args:
            z: Number
            N: Argument

        Returns:
            exp_z: Approximation of exponential function
        """
        exp_z = 1.0
        z_power = 1.0
        nfac = 1.0
        for n in range(1, N+1):
            nfac *= n
            z_power *= z
            exp_z += z_power / nfac
        return exp_z

    def exp_limit_compound(z, N):
        """Compute power series for exponential function

        Notebook: PCP_07_exp.ipynb

        Args:
            z: Number
            N: Argument

        Returns:
            exp_z: Approximation of exponential function
        """
        exp_z = (1 + z / N) ** N
        return exp_z

    z = 1
    print(f'Input argument z = {z:.0f}')
    for n in np.array([1, 2, 4, 8, 16, 32]):
        z0 = np.exp(z)
        z1 = exp_power_series(z, n)
        z2 = exp_limit_compound(z, n)
        print(f'N={n:3d}, Numpy={z0:.10f}, Approx1={z1:.10f}, Approx2={z2:.10f}')

    print('')
    z = 2 + 0.7*1j
    print(f'Input argument z = ({z.real:1.1f}, {z.imag:1.1f})')
    for n in np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512]):
        z0 = np.exp(z)
        z1 = exp_power_series(z, n)
        z2 = exp_limit_compound(z, n)
        print(f'N={n:3d}, Numpy=({z0.real:2.4f}, {z0.imag:2.4f}), Approx1=({z1.real:2.4f}, {z1.imag:2.4f}), Approx2=({z2.real:2.4f}, {z2.imag:2.4f})')


def exercise_gaussian(show_result=True):
    """Exercise 2: Gaussian Function

    Notebook: PCP_07_exp.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    def compute_gaussian_1D(X, mu=0, sigma=1):
        """Compute Gaussian function

        Notebook: PCP_07_exp.ipynb

        Args:
            X: array
            mu: Expected value (Default value = 0)
            sigma: Variance (Default value = 1)

        Returns:
            Y: Gaussian
        """
        Y = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp((-1 / 2) * (((X - mu) / sigma) ** 2))
        return Y

    x_min = -8
    x_max = 8
    x_delta = 0.01
    x = np.arange(x_min, x_max+x_delta, x_delta)

    plt.figure(figsize=(6.2, 2.5))
    plt.xlim([x_min, x_max])
    plt.ylim([0, 0.6])
    y1 = compute_gaussian_1D(x, mu=0, sigma=1)
    plt.plot(x, y1, 'r')

    y2 = compute_gaussian_1D(x, mu=-3, sigma=1.5)
    plt.plot(x, y2, 'b')

    y3 = compute_gaussian_1D(x, mu=+5, sigma=1)
    plt.plot(x, y3, 'k')

    y4 = compute_gaussian_1D(x, mu=2, sigma=0.8)
    plt.plot(x, y4, 'g')

    plt.legend([r'$\mu=0, \sigma=1$', r'$\mu=-3, \sigma=1.5$', r'$\mu=5, \sigma=1$', r'$\mu=2, \sigma=0.8$'],
               loc='upper left', framealpha=1)
    plt.xlim([x_min, x_max])
    plt.grid()
    plt.title('Different Gaussian functions')

    plt.tight_layout()


def exercise_spiral(show_result=True):
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
