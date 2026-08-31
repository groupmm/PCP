"""
Module: libpcp.unit06
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import os
import warnings
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def create_complex_plane(figsize=(4.5, 2),
                         xlim=(0, 1), ylim=(0, 1)):
    """Create a figure for visualizing complex numbers.

    Args:
        figsize: Figure width and height in inches.
        xlim: Limits of the real axis.
        ylim: Limits of the imaginary axis.
    """
    plt.figure(figsize=figsize, layout='tight')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$\operatorname{Re}$')
    plt.ylabel(r'$\operatorname{Im}$')
    plt.grid(alpha=0.3)
    plt.gca().set_axisbelow(True) 


def plot_complex_vector(c, start=0, color='black', linestyle='-'):
    """Plot the complex vector c beginning at start.

    Args:
        c: Complex number representing the vector.
        start: Complex number representing its starting point.
        color: Arrow color.
        linestyle: Arrow line style.

    Returns:
        Created Matplotlib arrow.
    """
    return plt.arrow(
        np.real(start), np.imag(start),
        np.real(c), np.imag(c),
        color=color, linestyle=linestyle,
        head_width=0.05, overhang=0.3,
        length_includes_head=True,
        zorder=3,        
    )


def exercise_rotate(show_result=True):
    """Exercise 1: Rotating Complex Numbers.

    Notebook: PCP_06_complex.ipynb

    Args:
        show_result: If True, display the resulting figures.
    """
    if not show_result:
        return

    # Construct c from its modulus and argument
    modulus = 1.2
    angle_degrees = 20
    angle = np.deg2rad(angle_degrees)
    c = modulus * (np.cos(angle) + 1j * np.sin(angle))

    c_conjugate = np.conj(c)
    c_inverse = 1 / c

    #print(f'c:               {c}')
    #print(f'conjugate:       {c_conjugate}')
    #print(f'inverse:         {c_inverse}')

    create_complex_plane(figsize=(3.5, 2), xlim=(-0.1, 1.7), ylim=(-0.6, 0.6))

    v1 = plot_complex_vector(c, color='black')
    v2 = plot_complex_vector(c_conjugate, color='blue')
    v3 = plot_complex_vector(c_inverse, color='red')

    plt.title('Complex Number, Conjugate, and Inverse')
    plt.legend([v1, v2, v3],
               ['$c$', r'$\overline{c}$', '$c^{-1}$'])

    def rotate_complex(c, angle_degrees):
        """Rotate a complex number clockwise.

        Args:
            c: Complex number to rotate.
            angle_degrees: Clockwise rotation angle in degrees.

        Returns:
            Rotated complex number.
        """
        angle = np.deg2rad(angle_degrees)
        rotation = np.cos(angle) - 1j * np.sin(angle)
        return c * rotation

    # Rotate c clockwise by several angles
    c = 1 + 0.5j
    angles = [15, 30, 45]
    colors = ['blue', 'green', 'red']

    create_complex_plane(figsize=(3.5, 2), xlim=(-0.1, 1.7), ylim=(-0.6, 0.6))
    handles = [plot_complex_vector(c, color='black')]

    for angle, color in zip(angles, colors):
        c_rotated = rotate_complex(c, angle)
        handles.append(plot_complex_vector(c_rotated, color=color))
        #print(f'Rotation by {angle:2d}°: {c_rotated}, '
        #      f'|c| = {np.abs(c_rotated):.6f}')

    labels = ['$c$', '$15^\\circ$', '$30^\\circ$', '$45^\\circ$']
    plt.title('Clockwise Rotations')
    plt.legend(handles, labels);


def exercise_polynomial(show_result=True):
    """Exercise 2: Visualizing Polynomial Roots.

    Notebook: PCP_06_complex.ipynb

    Args:
        show_result: If True, display the resulting figure.
    """
    if not show_result:
        return

    def visualize_roots(p, ax, title=''):
        """Compute and visualize the roots of a polynomial.

        Args:
            p: Polynomial coefficients in descending order of powers.
            ax: Matplotlib axis used for the visualization.
            title: Subplot title.
        """
        roots = np.roots(p)
        ax.scatter(np.real(roots), np.imag(roots), color='red', s=20)
        ax.set_title(title)
        ax.set_xlabel(r'$\operatorname{Re}$')
        ax.set_ylabel(r'$\operatorname{Im}$')
        ax.grid(alpha=0.3)

    polynomials = [
        (np.array([1, 0, -2]),
         '$p(z)=z^2-2$'),
        (np.array([1, 0, 2]),
         '$p(z)=z^2+2$'),
        (np.array([1, 0, 0, 0, 0, 0, 0, 0, -1]),
         '$p(z)=z^8-1$'),
        (np.array([1, 1, 1, 0, 0, 0, 0, 0, 0]),
         '$p(z)=z^8+z^7+z^6$'),
        (np.array([1, 1, 1, 0, 0, 0, 0, 0, 1e-6]),
         '$p(z)=z^8+z^7+z^6+10^{-6}$'),
        (np.array([1, 1-2j, 0, 3]),
         '$p(z)=z^3+(1-2i)z^2+3$'),
    ]

    fig, axes = plt.subplots(2, 3, figsize=(6.4, 4.2))

    for ax, (p, title) in zip(axes.flat, polynomials):
        visualize_roots(p, ax, title)

    plt.tight_layout()


def exercise_mandelbrot(show_result=True):
    """Exercise 3: Mandelbrot Set

    Notebook: PCP_06_complex.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    a_min = -2
    a_max = 1
    b_min = -1.2
    b_max = 1.2
    a_delta = 0.01
    b_delta = 0.01

    A, B = np.meshgrid(np.arange(a_min, a_max+a_delta, a_delta),
                       np.arange(b_min, b_max+b_delta, b_delta))
    M = A.shape[0]
    N = A.shape[1]
    C = A + B*1j

    iter_max = 50
    thresh = 100
    mandel = np.ones((M, N))

    for m in range(M):
        for n in range(N):
            c = C[m, n]
            z = 0
            for k in range(iter_max):
                z = z * z + c
                if np.abs(z) > thresh:
                    mandel[m, n] = 0
                    break

    plt.figure(figsize=(6.1, 4))
    extent = [a_min, a_max, b_min, b_max]
    plt.imshow(mandel, origin='lower', cmap='gray_r', extent=extent)
    plt.tight_layout()


def exercise_mandelbrot_fancy(show_result=True, save_file=False):
    """Exercise 3: Mandelbrot Set (more fancy version)

    Notebook: PCP_06_complex.ipynb

    Args:
        show_result: Show result (Default value = True)
        save_file: Save figure to .png (Default value = False)
    """
    if show_result is False:
        return

    a_min = -2
    a_max = 1
    b_min = -1.2
    b_max = 1.2
    a_delta = 0.005
    b_delta = 0.005

    A, B = np.meshgrid(np.arange(a_min, a_max+a_delta, a_delta),
                       np.arange(b_min, b_max+b_delta, b_delta))
    M = A.shape[0]
    N = A.shape[1]
    C = A + B*1j

    iter_max = 100
    thresh = 1000
    mandel_iter = np.zeros((M, N))

    warnings.filterwarnings('ignore')
    Z = np.zeros((M, N))
    for k in range(iter_max):
        Z = Z * Z + C
        ind = (np.abs(Z) > thresh)
        mandel_iter[ind] = k
        Z[ind] = np.nan

    Z[np.isnan(Z)] = thresh
    mandel = (np.abs(Z) < thresh).astype(int)

    color_wb = LinearSegmentedColormap.from_list('color_wb', [[1, 1, 1, 0], [0, 0, 0, 1]], N=2)

    plt.figure(figsize=(6.1, 4))
    extent = [a_min, a_max, b_min, b_max]
    plt.imshow(np.log(np.log(mandel_iter)), origin='lower', cmap='YlOrBr_r', extent=extent)
    plt.imshow(mandel, origin='lower', cmap=color_wb, extent=extent)
    plt.tight_layout()
    if save_file is True:
        output_path_filename = os.path.join('.', 'output', 'Mandelbrot.png')
        plt.savefig(output_path_filename)
