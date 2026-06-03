"""
Module: libpcp.vis
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


def exercise_vis1D(show_result=True):
    """Exercise 1: Plotting 1D Function

    Notebook: PCP_05_vis.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    Fs = 100
    t = np.arange(Fs+1) / Fs

    omega = 5
    x = np.sin(2 * np.pi * omega * t)

    plt.figure(figsize=(6, 1.5))
    plt.plot(t, x)

    plt.figure(figsize=(6, 1.5))
    plt.plot(t, x, color='red', linewidth=2, linestyle='-', marker='*')
    plt.ylabel('Amplitude')
    plt.xlabel('Time (seconds)')
    plt.title('Sinusoid of frequency $\omega=5$')
    plt.grid()

    plt.figure(figsize=(6, 1.5))
    plt.plot(t, x, color='blue', linewidth=1, linestyle=':', marker='.', markersize=10)
    plt.xlim((0, 1/omega))
    plt.ylabel('Amplitude')
    plt.xlabel('Time (seconds)')
    plt.title('One period of sinusoid')

    plt.figure(figsize=(6, 6))
    plt.subplot(3, 1, 1)
    plt.stem(t, x)
    plt.xlim((0, 1/omega))
    plt.ylabel('Amplitude')
    plt.xlabel('Time (seconds)')
    plt.title('Stem plot')

    plt.subplot(3, 1, 2)
    plt.step(t, x)
    plt.xlim((0, 1/omega))
    plt.ylabel('Amplitude')
    plt.xlabel('Time (seconds)')
    plt.title('Step plot')

    plt.subplot(3, 1, 3)
    plt.bar(t, x, width=0.003)
    plt.xlim((0, 1/omega))
    plt.ylabel('Amplitude')
    plt.xlabel('Time (seconds)')
    plt.title('Bar plot')

    plt.tight_layout()

    # plt.plot is the default command for displaying functions in a continuous way.
    # plt.stem is particularly suitable for emphasizing the discrete time instances.
    # plt.step is particularly suitable for emphasizing the values assumed by the discrete functions.
    # plt.bar is  particularly suitable for representing histograms.


def exercise_circle(show_result=True):
    """Exercise 2: Plotting Circle

    Notebook: PCP_05_vis.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    def plot_circle(Fs, ax):
        """Plot circle

        Notebook: PCP_05_vis.ipynb

        Args:
            Fs: Sampling rate
            ax: Axis handle
        """
        t = np.arange(Fs+1) / Fs
        f_1 = np.cos(2*np.pi*t)
        f_2 = np.sin(2*np.pi*t)
        ax.plot(f_1, f_2, color='red', linewidth=1, linestyle='-', marker='.')

    plt.figure(figsize=(10, 2.5))
    for i, Fs in enumerate([4, 8, 16, 32]):
        ax = plt.subplot(1, 4, i+1)
        plot_circle(Fs, ax)
    plt.tight_layout()


def exercise_logaxis(show_result=True):
    """Exercise 3: Plotting with Logarithmic Axes

    Notebook: PCP_05_vis.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    Fs = 100
    x = np.arange(1/Fs, 10, 1/Fs)
    f = np.exp(x)
    g = x
    h = 1.1 + np.sin(10*x)
    plt.figure(figsize=(12, 3))

    plt.subplot(1, 4, 1)
    plt.plot(x, f, x, g, x, h)
    plt.grid()
    plt.legend(['f', 'g', 'h'])
    plt.title('plt.plot')

    plt.subplot(1, 4, 2)
    plt.semilogy(x, f, x, g, x, h)
    plt.grid()
    plt.legend(['f', 'g', 'h'])
    plt.title('plt.semilogy')

    plt.subplot(1, 4, 3)
    plt.semilogx(x, f, x, g, x, h)
    plt.grid()
    plt.legend(['f', 'g', 'h'])
    plt.title('plt.semilogx')

    plt.subplot(1, 4, 4)
    plt.loglog(x, f, x, g, x, h)
    plt.grid()
    plt.legend(['f', 'g', 'h'])
    plt.title('plt.loglog')

    plt.tight_layout()


def exercise_plot3d(show_result=True):
    """Exercise 4: Plotting 3D Surface (sinc)

    Notebook: PCP_05_vis.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    X, Y = np.meshgrid(np.arange(-1, 1.01, 0.01), np.arange(-1, 1.01, 0.01))
    f = np.sinc(3*X) + np.sinc(3*Y)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X, Y, f, cmap='coolwarm')
    plt.show()

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(projection='3d')
    ax.plot_wireframe(X, Y, f)
    plt.show()


def exercise_erlangen(show_result=True):
    """Exercise 5: Photo Manipulation (Erlangen)

    Notebook: PCP_05_vis.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    img = mpimg.imread('./data/PCP_fig_erlangen.png')
    print('Size of image array (pixels, pixels, channels): ', img.shape)

    plt.figure(figsize=(12, 10))
    plt.subplot(3, 2, 1)
    plt.imshow(img)

    plt.subplot(3, 2, 2)
    plt.imshow(np.rot90(img, k=2))

    plt.subplot(3, 2, 3)
    rgb_weights = [0.2989, 0.5870, 0.1140]
    img_bw = rgb_weights[0] * img[:, :, 0] + rgb_weights[1]*img[:, :, 1] + rgb_weights[2]*img[:, :, 2]
    plt.imshow(img_bw, cmap='gray')

    plt.subplot(3, 2, 4)
    img_diff = np.maximum(np.abs(np.diff(img_bw, axis=0, append=0)), np.abs(np.diff(img_bw, axis=1, append=0)))
    plt.imshow(img_diff, cmap='gray_r')
    plt.clim((0, 0.5))

    plt.subplot(3, 2, 5)
    img_lum = img[:, :, 0]
    plt.imshow(img_lum, cmap='hot')

    plt.subplot(3, 2, 6)
    img_ds = img[1:-1:10, 1:-1:10, :]
    plt.imshow(img_ds)

    plt.tight_layout()

    mpimg.imsave('./output/PCP_fig_erlangen_mod.png', img_lum, cmap='hot')
