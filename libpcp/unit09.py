"""
Module: libpcp.unit09
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import numpy as np
from matplotlib import pyplot as plt
import IPython.display as ipd

from .unit08 import generate_sinusoid


def generate_example_signal(dur=1, sr=100):
    """Generate the example signal."""
    N = int(round(sr * dur))
    t = np.arange(N) / sr
    x =  0.8 * np.sin(2 * np.pi * (2 * t - 0.3))
    x += 0.5 * np.sin(2 * np.pi * (6 * t - 0.1))
    x += 0.3 * np.sin(2 * np.pi * (16 * t - 0.2))
    return x, t
    

def exercise_leakage(show_result=True):
    """Exercise 1: Frequency Bins and Spectral Leakage."""
    if not show_result:
        return

    sr = 64
    cases = [
        (10.0, 64, '10 Hz, one-second observation'),
        (10.5, 64, '10.5 Hz, one-second observation'),
        (10.5, 128, '10.5 Hz, two-second observation'),
    ]

    for freq, N, heading in cases:
        dur = N / sr
        x, _, _ = generate_sinusoid(dur=dur, freq=freq, sr=sr)
        X =  np.fft.fft(x)

        bin_spacing = sr / N
        bin_position = freq / bin_spacing
        lies_on_bin = np.isclose(bin_position, round(bin_position))

        # Nonnegative frequency bins and their unnormalized magnitudes
        k = np.arange(N // 2 + 1)
        freqs = k * bin_spacing
        magnitude = np.abs(X[:N // 2 + 1])

        print(heading)
        print(f'  sr:                   {sr} Hz')
        print(f'  N:                    {N}')
        print(f'  duration:             {dur:g} s')
        print(f'  bin spacing:          {bin_spacing:g} Hz')
        print(f'  theoretical bin:      k = {bin_position:g}')
        print(f'  lies on a DFT bin:    {"yes" if lies_on_bin else "no"}')

        fig, ax = plt.subplots(figsize=(5.2, 1.9), layout='tight')

        # A stem plot emphasizes the discrete frequency bins.
        markerline, stemlines, _ = ax.stem(
            freqs,
            magnitude,
            linefmt='k-',
            markerfmt='ko',
            basefmt=' ',
        )
        plt.setp(markerline, markersize=3)
        plt.setp(stemlines, linewidth=1)

        ax.axvline(
            freq,
            color='red',
            linestyle=':',
            linewidth=1.2,
            label=rf'$\omega={freq:g}\,\mathrm{{Hz}}$',
        )

        ax.set(
            xlabel='Frequency (Hz)',
            ylabel='Magnitude',
            xlim=(0, sr / 2),
            ylim=(0, 1.05 * magnitude.max()),
        )
        ax.grid(alpha=0.3)
        ax.legend(loc='upper right', framealpha=1)

        bin_axis = ax.secondary_xaxis(
            'top',
            functions=(
                lambda f, spacing=bin_spacing: f / spacing,
                lambda k, spacing=bin_spacing: k * spacing,
            ),
        )
        bin_axis.set_xlabel('Frequency index $k$')

        plt.show()



def plot_signal_dft_one_sided(
        x, X, sr, reference_freqs=None, figsize=(5.2, 3.0)):
    """Plot a signal and its one-sided DFT magnitude."""
    N = len(x)
    n = np.arange(N)
    t = n / sr

    k = np.arange(N // 2 + 1)
    freqs = k * sr / N
    magnitude = np.abs(X[:N // 2 + 1])

    data = [
        (t, x, rf'Signal $x$ ($N={N}$)', 'Time (seconds)'),
        (freqs, magnitude, 'One-Sided DFT Magnitude',
         'Frequency (Hertz)'),
    ]

    fig, axes = plt.subplots(
        len(data), 1,
        figsize=figsize,
        layout='tight',
    )

    for ax, (axis, values, title, xlabel) in zip(axes, data):
        ax.set(
            title=title,
            xlabel=xlabel,
            xlim=(axis[0], axis[-1]),
        )
        ax.grid(alpha=0.3)

    axes[0].plot(t, x, 'ko-', ms=2.5, lw=1.2)

    markerline, stemlines, _ = axes[1].stem(
        freqs,
        magnitude,
        linefmt='k-',
        markerfmt='ko',
        basefmt=' ',
    )
    plt.setp(markerline, markersize=3)
    plt.setp(stemlines, linewidth=1)
    axes[1].set_ylim(0, 1.05 * magnitude.max())

    if reference_freqs is not None:
        for index, freq in enumerate(reference_freqs, start=1):
                axes[1].axvline(
                    freq,
                    color='red',
                    linestyle=':',
                    linewidth=1.2
                )
    plt.show()


def exercise_missing_time(show_result=True):
    """Exercise 2: Frequency Content Without Time Localization."""
    if not show_result:
        return

    sr = 32
    T = 4
    N = T * sr

    freq_1 = 1.1
    freq_2 = 3.9
    amp_1 = 1
    amp_2 = 0.5

    t = np.arange(N) / sr

    sinusoid_1 = amp_1 * np.sin(2 * np.pi * freq_1 * t)
    sinusoid_2 = amp_2 * np.sin(2 * np.pi * freq_2 * t)

    # Both frequencies occur throughout the analysis interval.
    x_superposition = sinusoid_1 + sinusoid_2

    # The frequencies occur during different halves of the interval.
    x_concatenation = np.where(
        t < T / 2,
        sinusoid_1,
        sinusoid_2,
    )

    X_superposition = np.fft.fft(x_superposition)
    X_concatenation = np.fft.fft(x_concatenation)

    reference_freqs = [freq_1, freq_2]

    print('Superposition: Both frequencies occur throughout the signal')
    plot_signal_dft_one_sided(
        x_superposition,
        X_superposition,
        sr,
        reference_freqs=reference_freqs,
    )

    print('Concatenation: The frequencies occur at different times')
    plot_signal_dft_one_sided(
        x_concatenation,
        X_concatenation,
        sr,
        reference_freqs=reference_freqs,
    )

    
    
def generate_matrix_dft(N):
    """Generate the N x N DFT matrix."""
    n = np.arange(N)
    return np.exp(-2j * np.pi * n[:, None] * n / N)


def fft(x):
    """Compute the FFT recursively for a signal of power-of-two length."""
    x = np.asarray(x, dtype=np.complex128)
    N = len(x)
    assert N > 0 and np.log2(N).is_integer(), (
        'Signal length must be a power of two.'
    )

    if N == 1:
        return x

    # DFTs of the even- and odd-indexed samples
    A = fft(x[::2])
    B = fft(x[1::2])

    # Twiddle factors and butterfly operations
    k = np.arange(N // 2)
    C = np.exp(-2j * np.pi * k / N) * B
    return np.concatenate((A + C, A - C))
    
def exercise_dft_inverse(show_result=True):
    """Exercise 3: Inverse DFT and Signal Reconstruction."""
    if not show_result:
        return

    def generate_matrix_dft_inv(N):
        """Generate the N x N inverse DFT matrix."""
        k = np.arange(N)[:, None]
        n = np.arange(N)[None, :]
        return np.exp(2j * np.pi * k * n / N) / N
    
    def fft_inv(X):
        """Compute the inverse DFT using the forward FFT."""
        X = np.asarray(X, dtype=np.complex128)
        return np.conjugate(fft(np.conjugate(X))) / len(X)

    N = 32
    dft_mat = generate_matrix_dft(N)
    dft_inv_mat = generate_matrix_dft_inv(N)
    identity = np.eye(N)

    # Verify the inverse identities.
    print(
        'DFT @ DFT_inv equals identity:',
        np.allclose(dft_mat @ dft_inv_mat, identity),
    )
    print(
        'DFT_inv @ DFT equals identity:',
        np.allclose(dft_inv_mat @ dft_mat, identity),
    )

    # Compare with a general matrix inverse.
    print(
        'Explicit inverse agrees with np.linalg.inv:',
        np.allclose(dft_inv_mat, np.linalg.inv(dft_mat)),
    )

    # Transform and reconstruct a real-valued test signal.
    n = np.arange(N)
    x = (
        np.sin(2 * np.pi * 2 * n / N)
        + 0.5 * np.cos(2 * np.pi * 5 * n / N)
    )

    X = dft_mat @ x
    x_rec = dft_inv_mat @ X
    reconstruction_error = np.max(np.abs(x - x_rec))

    fig, ax = plt.subplots(figsize=(5.2, 2.0), layout='tight')
    ax.plot(n, x, 'ko-', ms=3, lw=1, label='Original')
    ax.plot(
        n,
        x_rec.real,
        'r.--',
        ms=3,
        lw=1,
        label='Reconstructed',
    )
    ax.set(
        title=f'Maximum reconstruction error: '
              f'{reconstruction_error:.2e}',
        xlabel='Sample index $n$',
        ylabel='Signal value',
        xlim=(n[0], n[-1]),
    )
    ax.grid(alpha=0.3)
    ax.legend(loc='upper right', framealpha=1)
    plt.show()

    # Compare the fast inverse with NumPy's implementation.
    X = fft(x)
    print(
        'fft_inv agrees with np.fft.ifft:',
        np.allclose(fft_inv(X), np.fft.ifft(X)),
    )


def generate_plucked_string(dur=2, freq=220, sr=16384):
    """Generate a plucked-string sound."""
    t = np.arange(int(dur * sr)) / sr

    # Add the fundamental and its harmonics
    harmonics = (1, 0.7, 0.5, 0.35, 0.25, 0.18, 0.12, 0.08)
    x = sum(
        amp * np.sin(2 * np.pi * k * freq * t)
        for k, amp in enumerate(harmonics, start=1)
    )

    # Create the attack, gradual decay, and release
    envelope = np.exp(-2 * t)
    n_attack = int(0.005 * sr)
    n_release = int(0.25 * sr)
    envelope[:n_attack] *= np.linspace(0, 1, n_attack)
    envelope[-n_release:] *= np.linspace(1, 0, n_release)
    x *= envelope

    # Prevent clipping
    x *= 0.8 / np.max(np.abs(x))
    return x, t, sr

def exercise_sound_modification(show_result=True):
    """Exercise 4: Modifying a Sound in the Frequency Domain."""
    if not show_result:
        return

    def plot_sound_dft(x, t, sr, title, freq_max=2500):
        """Plot a sound and its one-sided DFT magnitude, then play it."""
        N = len(x)
        k = np.arange(int(freq_max * N / sr) + 1)
        freqs = k * sr / N
        magnitude = np.abs(np.fft.fft(x)[k])

        fig, axes = plt.subplots(1, 2, figsize=(6.2, 1.9), layout='tight')

        axes[0].plot(t, x, color='black', linewidth=0.5)
        axes[0].set(
            title=title,
            xlabel='Time (seconds)',
            xlim=(t[0], t[-1]),
            ylim=(-1, 1),
        )

        axes[1].plot(freqs, magnitude, color='black', linewidth=0.8)
        axes[1].set(
            title='One-Sided DFT Magnitude',
            xlabel='Frequency (Hz)',
            xlim=(0, freq_max),
        )

        for ax in axes:
            ax.grid(alpha=0.3)

        plt.show()
        ipd.display(ipd.Audio(x, rate=sr, normalize=False))

    x, t, sr = generate_plucked_string()
    X = np.fft.fft(x)
    freqs = np.fft.fftfreq(len(x), d=1 / sr)

    # Analysis: the peaks occur at integer multiples of 220 Hz.
    plot_sound_dft(x, t, sr, 'Original Sound')

    # Changing magnitudes: remove positive and negative frequencies.
    X_low = X.copy()
    X_low[np.abs(freqs) > 500] = 0
    x_low = np.fft.ifft(X_low)
    plot_sound_dft(x_low.real, t, sr, 'Frequencies Above 500 Hz Removed')

    # print(
    #     'Largest imaginary part:',
    #     f'{np.max(np.abs(x_low.imag)):.2e}',
    # )

    # Changing phases: conjugation reverses the sound in time.
    x_conj = np.fft.ifft(np.conj(X)).real
    plot_sound_dft(x_conj, t, sr, 'Phases Reversed')
