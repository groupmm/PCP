"""
Module: libpcp.unit06
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import os
import numpy as np
from matplotlib import pyplot as plt

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
    """Exercise 3: Approximating the Mandelbrot Set.

    Notebook: PCP_06_complex.ipynb

    Args:
        show_result: If True, display the resulting figure.
    """
    if not show_result:
        return

    def approximate_mandelbrot(a_range=(-2, 1), b_range=(-1.2, 1.2),
                               spacing=0.01, max_iterations=100):
        """Approximate the Mandelbrot set on a rectangular grid.

        Args:
            a_range: Minimum and maximum real coordinates.
            b_range: Minimum and maximum imaginary coordinates.
            spacing: Spacing between neighboring grid points.
            max_iterations: Maximum number of iterations per point.

        Returns:
            Real coordinates, imaginary coordinates, and indicator array.
        """
        a = np.arange(a_range[0], a_range[1] + spacing / 2, spacing)
        b = np.arange(b_range[0], b_range[1] + spacing / 2, spacing)
        A, B = np.meshgrid(a, b)
        C = A + 1j * B

        indicator = np.ones(C.shape, dtype=int)

        for m in range(C.shape[0]):
            for n in range(C.shape[1]):
                c = C[m, n]
                z = 0

                for _ in range(max_iterations):
                    z = z**2 + c

                    if abs(z) > 2:
                        indicator[m, n] = 0
                        break

        return a, b, indicator

    a, b, indicator = approximate_mandelbrot()

    coordinate_extent = [a[0], a[-1], b[0], b[-1]]

    plt.figure(figsize=(6.1, 4), layout='tight')
    plt.imshow(
        indicator,
        cmap='gray_r',
        origin='lower',
        extent=coordinate_extent,
        interpolation='nearest',
    )
    plt.title('Approximation of the Mandelbrot Set')
    plt.xlabel(r'$\operatorname{Re}(c)$')
    plt.ylabel(r'$\operatorname{Im}(c)$');


def exercise_mandelbrot_fancy(show_result=True, save_file=False):
    """Exercise 3: Colored approximation of the Mandelbrot set.

    Notebook: PCP_06_complex.ipynb

    Args:
        show_result: If True, display the resulting figure.
        save_file: If True, save the figure as a PNG file.
    """
    if not show_result:
        return

    # Coordinate grid
    a_min, a_max = -2, 1
    b_min, b_max = -1.2, 1.2
    spacing = 0.005

    a = np.arange(a_min, a_max + spacing / 2, spacing)
    b = np.arange(b_min, b_max + spacing / 2, spacing)
    A, B = np.meshgrid(a, b)
    C = A + 1j * B

    # Escape-time iteration
    max_iterations = 100
    Z = np.zeros(C.shape, dtype=complex)
    active = np.ones(C.shape, dtype=bool)
    escape_iteration = np.zeros(C.shape)

    for k in range(max_iterations):
        Z[active] = Z[active]**2 + C[active]
        escaped = active & (np.abs(Z) > 2)
        escape_iteration[escaped] = k + 2
        active[escaped] = False

    # Apply logarithmic escape-time coloring
    color_values = np.log(np.maximum(escape_iteration, 2))
    color_values = np.ma.array(color_values, mask=active)

    colormap = plt.get_cmap('YlOrBr_r').copy()
    colormap.set_bad('black')

    #color_min = np.log(2)
    #color_max =np.log(max_iterations + 1)
    # Select color limits for a visually balanced image
    color_min = 1.2
    color_max = 3.3
    coordinate_extent = [a_min, a_max, b_min, b_max]

    plt.figure(figsize=(6.1, 4), layout='tight')
    plt.imshow(
        color_values,
        cmap=colormap,
        origin='lower',
        extent=coordinate_extent,
        interpolation='nearest',
        vmin=color_min,
        vmax=color_max,
    )
    plt.title('Mandelbrot Set with Escape-Time Coloring')
    plt.xlabel(r'$\operatorname{Re}(c)$')
    plt.ylabel(r'$\operatorname{Im}(c)$')

    if save_file:
        output_path = os.path.join('.', 'output', 'Mandelbrot.png')
        plt.savefig(output_path)