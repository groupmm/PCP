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


def generate_figure(figsize=(4.5, 2.0), xlim=[0, 1], ylim=[0, 1]):
    """Generate figure for plotting complex numbers

    Notebook: PCP_06_complex.ipynb

    Args:
       figsize: Width, height in inches (Default value = (2, 2))
       xlim: Limits for x-axis (Default value = [0, 1])
       ylim: Limits for y-axis (Default value = [0, 1])
    """
    plt.figure(figsize=figsize)
    plt.grid()
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$\mathrm{Re}$')
    plt.ylabel(r'$\mathrm{Im}$')


def plot_vector(c, color='k', start=0, linestyle='-'):
    """Plot arrow corresponding to difference of two complex numbers

    Notebook: PCP_06_complex.ipynb

    Args:
        c: Complex number
        color: Color of arrow (Default value = 'k')
        start: Complex number encoding the start position (Default value = 0)
        linestyle: Linestyle of arrow (Default value = '-')

    Returns:
        plt.arrow: matplotlib.patches.FancyArrow
    """
    return plt.arrow(np.real(start), np.imag(start), np.real(c), np.imag(c),
                     linestyle=linestyle, head_width=0.05,
                     fc=color, ec=color, overhang=0.3, length_includes_head=True)


def plot_polar_vector(c, label=None, color=None, start=0, linestyle='-'):
    """Plot arrow in polar plot

    Notebook: PCP_06_complex.ipynb

    Args:
        c: Complex number
        label: Label of arrow (Default value = None)
        color: Color of arrow (Default value = None)
        start: Complex number encoding the start position (Default value = 0)
        linestyle: Linestyle of arrow (Default value = '-')
    """
    # plot line in polar plane
    line = plt.polar([np.angle(start), np.angle(c)], [np.abs(start), np.abs(c)], label=label,
                     color=color, linestyle=linestyle)
    # plot arrow in same color
    this_color = line[0].get_color() if color is None else color
    plt.annotate('', xytext=(np.angle(start), np.abs(start)), xy=(np.angle(c), np.abs(c)),
                 arrowprops=dict(facecolor=this_color, edgecolor='none',
                                 headlength=12, headwidth=10, shrink=1, width=0))


def exercise_complex(show_result=True):
    """Exercise 1: Rotate Complex Number

    Notebook: PCP_06_complex.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    c_abs = 1.2
    c_angle = 20  # in degree
    c_angle_rad = np.deg2rad(c_angle)
    a = c_abs * np.cos(c_angle_rad)
    b = c_abs * np.sin(c_angle_rad)
    c = a + b*1j
    c_conj = np.conj(c)
    c_inv = 1 / c
    generate_figure(xlim=[-0.25, 1.75], ylim=[-0.5, 0.5])
    v1 = plot_vector(c, color='k')
    v2 = plot_vector(c_conj, color='b')
    v3 = plot_vector(c_inv, color='r')
    plt.legend([v1, v2, v3], ['$c$', r'$\overline{c}$', '$c^{-1}$'])

    def rotate_complex(c, r):
        """Rotate complex number

        Notebook: PCP_06_complex.ipynb

        Args:
            c: Complex number
            r: Angle in degrees
        """
        c_angle_rad = np.angle(c) - np.deg2rad(r)
        c_abs = np.abs(c)
        a = c_abs * np.cos(c_angle_rad)
        b = c_abs * np.sin(c_angle_rad)
        c_rot = a + b*1j
        return c_rot

    c = 1 + 0.5*1j
    generate_figure(xlim=[-0.25, 1.75], ylim=[-0.25, 0.75])
    v1 = plot_vector(c, color='k')
    v2 = plot_vector(rotate_complex(c, 10), color='b')
    v3 = plot_vector(rotate_complex(c, 20), color='g')
    v4 = plot_vector(rotate_complex(c, 30), color='r')
    plt.legend([v1, v2, v3, v4], ['$c$', '$r=10$', '$r=20$', '$r=30$'])


def exercise_polynomial(show_result=True):
    """Exercise 2: Roots of Polynomial

    Notebook: PCP_06_complex.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    def vis_root(p, ax, title=''):
        """Visualize roots of polynomial

        Notebook: PCP_06_complex.ipynb

        Args:
            p: Polynomial coefficients
            ax: Axis handle
            title: Plot title (Default value = '')
        """
        poly_root = np.roots(p)
        ax.scatter(np.real(poly_root), np.imag(poly_root), color='red', s=20)
        ax.grid()
        ax.set_title(title)
        ax.set_xlabel(r'$\mathrm{Re}$')
        ax.set_ylabel(r'$\mathrm{Im}$')

    fig, ax = plt.subplots(3, 2, figsize=(5, 7))

    p = np.array([1, 0, -2])
    vis_root(p, ax[0, 0], title='$p(z)=z^2-2$')

    p = np.array([1, 0, 2])
    vis_root(p, ax[0, 1], title='$p(z)=z^2+2$')

    p = np.array([1, 0, 0, 0, 0, 0, 0, 0, -1])
    vis_root(p, ax[1, 0], '$p(z)=z^8-1$')

    p = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0])
    vis_root(p, ax[1, 1], '$p(z)=z^8 + z^7 + z^6$')

    p = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0.000001])
    vis_root(p, ax[2, 0], '$p(z)=z^8 + z^7 + z^6 + 0.000001$')

    p = np.array([1, -2j, 2 + 4j, 3])
    vis_root(p, ax[2, 1], '$p(z)=z^3 -2iz^2 + (2+4i)z + 3 $')

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
