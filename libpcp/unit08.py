"""
Module: libpcp.unit08
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import numpy as np
from matplotlib import pyplot as plt
import IPython.display as ipd


def generate_sinusoid(dur=1, amp=1, freq=1, phase=0, Fs=100):
    """Generation of sinusoid

    Notebook: PCP_08_signal.ipynb

    Args:
        dur: Duration (in seconds) of sinusoid (Default value = 1)
        amp: Amplitude of sinusoid (Default value = 1)
        freq: Frequency (in Hertz) of sinusoid (Default value = 1)
        phase: Phase (relative to interval [0,1)) of sinusoid (Default value = 0)
        Fs: Sampling rate (in samples per second) (Default value = 100)

    Returns:
        x: Signal
        t: Time axis (in seconds)
    """
    num_samples = int(Fs * dur)
    t = np.arange(num_samples) / Fs
    x = amp * np.sin(2 * np.pi * (freq * t - phase))
    return x, t


def generate_example_signal(dur=1, Fs=100):
    """Generate example signal

    Notebook: PCP_08_signal.ipynb

    Args:
        dur: Duration (in seconds) of signal (Default value = 1)
        Fs: Sampling rate (in samples per second) (Default value = 100)

    Returns:
        x: Signal
        t: Time axis (in seconds)
    """
    N = int(Fs * dur)
    t = np.arange(N) / Fs
    x = 1 * np.sin(2 * np.pi * (1.9 * t - 0.3))
    x += 0.5 * np.sin(2 * np.pi * (6.1 * t - 0.1))
    x += 0.1 * np.sin(2 * np.pi * (20 * t - 0.2))
    return x, t


def sampling_equidistant(x_1, t_1, Fs_2, dur=None):
    """Equidistant sampling of interpolated signal

    Notebook: PCP_08_signal.ipynb

    Args:
        x_1: Signal to be interpolated and sampled
        t_1: Time axis (in seconds) of x_1
        Fs_2: Sampling rate used for equidistant sampling
        dur: Duration (in seconds) of sampled signal (Default value = None)

    Returns:
        x_2: Sampled signal
        t_2: time axis (in seconds) of sampled signal
    """
    if dur is None:
        dur = len(t_1) * t_1[1]
    N = int(Fs_2 * dur)
    t_2 = np.arange(N) / Fs_2
    x_2 = np.interp(t_2, t_1, x_1)
    return x_2, t_2


def reconstruction_sinc(x, t, t_sinc):
    """Reconstruction from sampled signal using sinc-functions

    Notebook: PCP_08_signal.ipynb

    Args:
        x: Sampled signal
        t: Equidistant discrete time axis (in seconds) of x
        t_sinc: Equidistant discrete time axis (in seconds) of signal to be reconstructed

    Returns:
        x_sinc: Reconstructed signal having time axis t_sinc
    """
    Fs = 1 / t[1]
    x_sinc = np.zeros(len(t_sinc))
    for n in range(0, len(t)):
        x_sinc += x[n] * np.sinc(Fs * t_sinc - n)
    return x_sinc


def plot_signal_reconstructed(t_1, x_1, t_2, x_2, t_sinc, x_sinc, figsize=(6.2, 2.0)):
    """Plotting three signals

    Notebook: PCP_08_signal.ipynb

    Args:
        t_1: Time axis of original signal
        x_1: Original signal
        t_2: Time axis for sampled signal
        x_2: Sampled signal
        t_sinc: Time axis for reconstructed signal
        x_sinc: Reconstructed signal
        figsize: Figure size (Default value = (8, 2.2))
    """
    plt.figure(figsize=figsize)
    plt.plot(t_1, x_1, 'k', linewidth=1, linestyle='dotted', label='Orignal signal')
    plt.stem(t_2, x_2, linefmt='r:', markerfmt='r.', basefmt='None', label='Samples')
    plt.plot(t_sinc, x_sinc, 'b', label='Reconstructed signal')
    plt.title(r'Sampling rate $F_\mathrm{s} = %.0f$' % (1/t_2[1]))
    plt.xlabel('Time (seconds)')
    plt.ylim([-1.8, 1.8])
    plt.xlim([t_1[0], t_1[-1]])
    plt.legend(loc='upper right', framealpha=1)
    plt.tight_layout()
    plt.show()


def plot_interference(t, x1, x2, figsize=(6.2, 2.0), xlim=None, ylim=None, title=''):
    """Plotting two signals and its superposition

    Notebook: PCP_08_signal.ipynb

    Args:
        t: Time axis
        x1: Signal 1
        x2: Signal 2
        figsize: Figure size (Default value = (8, 2))
        xlim: x-Axis limits (Default value = None)
        ylim: y-Axis limits (Default value = None)
        title: Figure title (Default value = '')
    """
    plt.figure(figsize=figsize)
    plt.plot(t, x1, color='gray', linewidth=1.0, linestyle='-', label='x1')
    plt.plot(t, x2, color='cyan', linewidth=1.0, linestyle='-', label='x2')
    plt.plot(t, x1+x2, color='red', linewidth=2.0, linestyle='-', label='x1+x2')
    if xlim is None:
        plt.xlim([0, t[-1]])
    else:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()


def exercise_beating(show_result=True):
    """Exercise 1: Beating

    Notebook: PCP_08_signal.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    Fs = 100
    dur = 5
    omega_1 = 10
    omega_2 = 11
    x1, t = generate_sinusoid(dur=dur, Fs=Fs, amp=0.5, freq=omega_1)
    x2, t = generate_sinusoid(dur=dur, Fs=Fs, amp=0.5, freq=omega_2)
    title = r'Beating with $\omega_1=%.1f$ and $\omega_2=%.1f$ (beating period: %.1f)' % \
        (omega_1, omega_2, np.abs(omega_2-omega_1))
    plot_interference(t, x1, x2, ylim=[-1.1, 1.1], xlim=[0, dur], title=title)
    plot_interference(t, x1, x2, ylim=[-1.1, 1.1], xlim=[1, 2], title=r'Zoom-in section')

    Fs = 4000
    dur = 5
    omega_1 = 200
    omega_2 = 203
    x1, t = generate_sinusoid(dur=dur, Fs=Fs, amp=0.5, freq=omega_1)
    x2, t = generate_sinusoid(dur=dur, Fs=Fs, amp=0.5, freq=omega_2)
    title = r'Beating with $\omega_1=%.1f$ and $\omega_2=%.1f$ (beating frequency: %.1f)' \
        % (omega_1, omega_2, np.abs(omega_2-omega_1))
    plot_interference(t, x1, x2, ylim=[-1.1, 1.1], xlim=[0, dur], title=title)

    ipd.display(ipd.Audio(x1+x2, rate=Fs))


def exercise_aliasing_sinus(show_result=True):
    """Exercise 2: Aliasing with Sinsuoids

    Notebook: PCP_08_signal.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    x, t = generate_sinusoid(dur=2, Fs=128, freq=10)

    figsize = (6.2, 2.0)
    plt.figure(figsize=figsize)
    plt.plot(t, x, 'k')
    plt.title('Original CT-signal')
    plt.xlabel('Time (seconds)')
    plt.ylim([-1.5, 1.5])
    plt.xlim([t[0], t[-1]])
    plt.tight_layout()

    for Fs_2 in np.array([64, 32, 20, 16, 12, 8, 4]):
        x_2, t_2 = sampling_equidistant(x, t, Fs_2)
        t_sinc = t
        x_sinc = reconstruction_sinc(x_2, t_2, t_sinc)
        plot_signal_reconstructed(t, x, t_2, x_2, t_sinc, x_sinc, figsize=figsize)


def exercise_aliasing_visual(show_result=True):
    """Exercise 3: Visual Aliasing

    Notebook: PCP_08_signal.ipynb

    Args:
        show_result: Show result (Default value = True)
    """
    if show_result is False:
        return

    import IPython.display as ipd
    ipd.display(ipd.YouTubeVideo('QOwzkND_ooU', width=600, height=450))
