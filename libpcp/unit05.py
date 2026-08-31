"""
Module: libpcp.unit05
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


def exercise_vis1D(show_result=True):
    """Exercise 1: Visualizing a Sampled Sinusoid.

    Notebook: PCP_05_vis.ipynb

    Args:
        show_result: If True, display the resulting figures.
    """
    if not show_result:
        return

    # Construct the time axis and sampled sinusoid
    Fs = 100
    omega = 5
    period = 1 / omega

    t = np.arange(Fs + 1) / Fs
    x = np.sin(2 * np.pi * omega * t)

    # Plot the complete signal
    plt.figure(figsize=(4.0, 1.8), layout='tight')
    plt.plot(
        t,
        x,
        color='red',
        linewidth=1.5,
        linestyle='-',
        marker='o',
        markersize=3,
    )
    plt.title(r'Sampled Sinusoid ($\omega=5\,\mathrm{Hz}$)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.xlim(0, 1)
    plt.ylim(-1.1, 1.1)
    plt.grid(alpha=0.3)

    # Select the samples belonging to the first period
    period_mask = t <= period
    t_period = t[period_mask]
    x_period = x[period_mask]

    # Compare four plotting styles
    plt.figure(figsize=(5.2, 3.6), layout='tight')

    plt.subplot(2, 2, 1)
    plt.plot(
        t_period,
        x_period,
        color='lightgray',
        linewidth=2,
        marker='o',
        markerfacecolor='red',
        markeredgecolor='black',
        markersize=4,
    )
    plt.title('Line Plot with Markers')
    plt.ylabel('Amplitude')
    plt.xlim(0, period)
    plt.ylim(-1.1, 1.1)
    plt.grid(alpha=0.3)

    plt.subplot(2, 2, 2)
    stem = plt.stem(
        t_period,
        x_period,
        linefmt='black',
        markerfmt='ro',
        basefmt='gray',
    )
    stem.markerline.set_markersize(4)
    plt.title('Stem Plot')
    plt.xlim(0, period)
    plt.ylim(-1.1, 1.1)
    plt.grid(alpha=0.3)

    plt.subplot(2, 2, 3)
    plt.step(t_period, x_period, where='post', color='blue')
    plt.title('Step Plot')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.xlim(0, period)
    plt.ylim(-1.1, 1.1)
    plt.grid(alpha=0.3)

    plt.subplot(2, 2, 4)
    plt.bar(
        t_period,
        x_period,
        width=0.007,
        color='orange',
        edgecolor='black',
    )
    plt.title('Bar Plot')
    plt.xlabel('Time (seconds)')
    plt.xlim(0, period)
    plt.ylim(-1.1, 1.1)
    plt.grid(alpha=0.3)

    # The line plot visually interpolates between neighboring samples.
    # The stem plot emphasizes the individual sampling positions.
    # The step plot suggests piecewise-constant values between samples.
    # The bar plot represents each value through the height of a filled bar.


def exercise_circle(show_result=True):
    """Exercise 2: Approximating a Circle with Samples.

    Notebook: PCP_05_vis.ipynb

    Args:
        show_result: If True, display the resulting figures.
    """
    if not show_result:
        return

    def plot_circle(Fs, equal_aspect=True):
        """Plot a sampled approximation of the unit circle.

        Args:
            Fs: Positive integer specifying the sampling rate.
            equal_aspect: If True, use equal scaling on both axes.
        """
        t = np.linspace(0, 1, Fs + 1)
        f1 = np.cos(2 * np.pi * t)
        f2 = np.sin(2 * np.pi * t)
        # Since f1**2 + f2**2 = 1, every pair (f1, f2)
        # lies on the unit circle, apart from rounding errors.        

        plt.plot(
            f1,
            f2,
            color='lightgray',
            linewidth=1.5,
            marker='o',
            markersize=4,
            markerfacecolor='red',
            markeredgecolor='black',
        )
        plt.xlabel('$f_1(t)$')
        plt.ylabel('$f_2(t)$')
        plt.xlim(-1.1, 1.1)
        plt.ylim(-1.1, 1.1)
        plt.grid(alpha=0.3)

        if equal_aspect:
            plt.axis('equal')

    # Compare default and equal axis scaling
    plt.figure(figsize=(5.2, 1.8), layout='tight')

    plt.subplot(1, 2, 1)
    plot_circle(32, equal_aspect=False)
    plt.title('Default Aspect Ratio')

    plt.subplot(1, 2, 2)
    plot_circle(32, equal_aspect=True)
    plt.title('Equal Aspect Ratio')

    # Compare different sampling rates
    plt.figure(figsize=(4.0, 4.0), layout='tight')

    for index, Fs in enumerate([4, 8, 16, 32]):
        plt.subplot(2, 2, index + 1)
        plot_circle(Fs, equal_aspect=True)
        plt.title(rf'$F_\mathrm{{s}} = {Fs}$')


def exercise_logaxis(show_result=True):
    """Exercise 3: Comparing Linear and Logarithmic Axes.

    Notebook: PCP_05_vis.ipynb

    Args:
        show_result: If True, display the resulting figure.
    """
    if not show_result:
        return

    Fs = 100

    # Start above zero because logarithmic axes require positive values
    x = np.arange(1 / Fs, 10 + 1 / Fs, 1 / Fs)

    y_exp = np.exp(x)
    y_linear = x + 0.1
    y_oscillation = np.sin(10 * x) + 1.1

    plt.figure(figsize=(5.2, 4), layout='tight')

    plt.subplot(2, 2, 1)
    plt.plot(x, y_exp, x, y_linear, x, y_oscillation)
    plt.title('Linear Axes')
    plt.xlabel('$x$')
    plt.ylabel('Function value')
    plt.legend(['$f$', '$g$', '$h$'])
    plt.grid(alpha=0.3)

    plt.subplot(2, 2, 2)
    plt.semilogy(x, y_exp, x, y_linear, x, y_oscillation)
    plt.title('Logarithmic Vertical Axis')
    plt.xlabel('$x$')
    plt.ylabel('Function value')
    plt.legend(['$f$', '$g$', '$h$'])
    plt.grid(alpha=0.3)

    plt.subplot(2, 2, 3)
    plt.semilogx(x, y_exp, x, y_linear, x, y_oscillation)
    plt.title('Logarithmic Horizontal Axis')
    plt.xlabel('$x$')
    plt.ylabel('Function value')
    plt.legend(['$f$', '$g$', '$h$'])
    plt.grid(alpha=0.3)

    plt.subplot(2, 2, 4)
    plt.loglog(x, y_exp, x, y_linear, x, y_oscillation)
    plt.title('Both Axes Logarithmic')
    plt.xlabel('$x$')
    plt.ylabel('Function value')
    plt.legend(['$f$', '$g$', '$h$'])
    plt.grid(alpha=0.3)

def exercise_erlangen(show_result=True):
    """Exercise 4: Manipulating a Digital Photograph.

    Notebook: PCP_05_vis.ipynb

    Args:
        show_result: If True, display and save the modified images.
    """
    if not show_result:
        return

    # Load and inspect the RGB image
    image = mpimg.imread('./data/PCP_fig_erlangen.png')
    print('Image shape (rows, columns, channels):', image.shape)

    # Convert the image to grayscale using perceptual RGB weights
    image_gray = (
        0.2989 * image[:, :, 0]
        + 0.5870 * image[:, :, 1]
        + 0.1140 * image[:, :, 2]
    )

    # Approximate changes in intensity along both array dimensions
    difference_vertical = np.abs(
        np.diff(image_gray, axis=0, append=image_gray[-1:, :])
    )
    difference_horizontal = np.abs(
        np.diff(image_gray, axis=1, append=image_gray[:, -1:])
    )
    image_edges = np.maximum(difference_vertical, difference_horizontal)

    # Extract one color channel and create a downsampled image
    red_channel = image[:, :, 0]
    image_downsampled = image[::10, ::10, :]

    plt.figure(figsize=(5.2, 6), layout='tight')

    plt.subplot(3, 2, 1)
    plt.imshow(image)
    plt.title('Original')

    plt.subplot(3, 2, 2)
    plt.imshow(np.rot90(image, k=2))
    plt.title(r'Rotation by $180^\circ$')

    plt.subplot(3, 2, 3)
    plt.imshow(image_gray, cmap='gray')
    plt.title('Grayscale')

    plt.subplot(3, 2, 4)
    plt.imshow(image_edges, cmap='gray_r', vmin=0, vmax=0.5)
    plt.title('Intensity Differences')

    plt.subplot(3, 2, 5)
    plt.imshow(red_channel, cmap='hot')
    plt.title('Red Channel with Hot Colormap')

    plt.subplot(3, 2, 6)
    plt.imshow(image_downsampled)
    plt.title('Every Tenth Pixel')

    # The output directory must already exist
    mpimg.imsave(
        './output/PCP_fig_erlangen_mod.png',
        red_channel,
        cmap='hot',
    )
