"""
Module: libpcp.unit08
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

import numpy as np
from matplotlib import pyplot as plt
import IPython.display as ipd

def generate_sinusoid(dur=1, amp=1, freq=1, phase=0, sr=4000):
    """Generate a sampled sinusoid."""
    t = np.arange(int(dur * sr)) / sr
    x = amp * np.sin(2 * np.pi * (freq * t - phase))
    return x, t, sr

def sampling_equidistant(x_ref, t_ref, sr, dur=None):
    """Sample an interpolated reference signal at equally spaced times."""
    if dur is None:
        dur = t_ref[-1] + t_ref[1] - t_ref[0]
    N = int(round(sr * dur))
    t = np.arange(N) / sr
    x = np.interp(t, t_ref, x_ref)
    return x, t


def reconstruction_sinc(x, t, t_rec):
    """Reconstruct a sampled signal using sinc interpolation."""
    sr = 1 / (t[1] - t[0])
    x_rec = np.zeros_like(t_rec)
    for n, value in enumerate(x):
        x_rec += value * np.sinc(sr * t_rec - n)
    return x_rec


def plot_reconstruction(x_ref, t_ref, x, t, x_rec, figsize=(6.2, 1.7)):
    """Plot a reference, sampled, and reconstructed signal."""
    sr = 1 / (t[1] - t[0])
    dur = t_ref[-1] + t_ref[1] - t_ref[0]

    plt.figure(figsize=figsize, layout='tight')
    plt.plot(t_ref, x_ref, 'k:', linewidth=1,
             label='Reference')
    markers, stems, _ = plt.stem(
        t, x, linefmt='r-', markerfmt='ro',
        basefmt=' ', label='Samples'
    )
    markers.set_markersize(3)
    stems.set_linewidth(0.8)
    markers.set_zorder(3)
    stems.set_zorder(3)
    plt.plot(t_ref, x_rec, color='blue', label='Reconstruction')
    plt.title(rf'Sampling rate $F_\mathrm{{s}}={sr:g}$ Hz')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Signal value')
    plt.xlim(0, dur)
    plt.ylim(-1.8, 1.8)
    plt.grid(alpha=0.3)
    plt.legend(loc='upper right', framealpha=1)
    plt.show()
    
def exercise_aliasing_sinus(show_result=True):
    """Exercise 2: Aliasing with Sinusoids.

    Notebook: PCP_08_signal.ipynb

    Args:
        show_result: If True, display the resulting figures.
    """
    if not show_result:
        return

    # Generate a densely sampled reference signal
    dur = 2
    x_ref, t_ref, _ = generate_sinusoid(dur=dur, freq=9.99, sr=128)

    plt.figure(figsize=(6.2, 1.7), layout='tight')
    plt.plot(t_ref, x_ref, color='black', label='Reference')
    plt.title('Densely Sampled Reference Signal')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Signal value')
    plt.xlim(0, dur)
    plt.ylim(-1.5, 1.5)
    plt.grid(alpha=0.3)
    plt.legend(loc='upper right', framealpha=1)
    plt.show()

    # Sample and reconstruct at decreasing sampling rates
    for sr in [64, 32, 20, 16, 12, 8, 4]:
        x, t = sampling_equidistant(x_ref, t_ref, sr=sr)
        x_rec = reconstruction_sinc(x, t, t_ref)
        plot_reconstruction(
            x_ref, t_ref, x, t, x_rec, figsize=(6.2, 1.7)
        )    

def exercise_sinc(show_result=True):
    """Exercise 2: Understanding Sinc Interpolation."""
    if not show_result:
        return

    x = np.array([0, 1, -0.5, 0.75, 0])
    n = np.arange(len(x))
    t = np.linspace(-2, 6, 801)

    def sinc_reconstruction(x, t):
        """Reconstruct samples using sinc interpolation with T=1."""
        return sum(x[k] * np.sinc(t - k) for k in range(len(x)))

    def create_axes():
        """Create axes with a fixed region for an external legend."""
        fig, ax = plt.subplots(figsize=(6.2, 1.9))
        fig.subplots_adjust(
            left=0.10, right=0.68, bottom=0.23, top=0.82
        )
        return ax

    def add_legend(ax):
        """Place the legend in the reserved region."""
        ax.legend(
            loc='upper left',
            bbox_to_anchor=(1.02, 1),
            borderaxespad=0,
            fontsize=7,
            framealpha=1,
        )

    # Plot the normalized sinc function
    t_sinc = np.linspace(-4, 4, 801)
    integers = np.arange(-4, 5)

    ax = create_axes()
    ax.plot(t_sinc, np.sinc(t_sinc), color='black',
            label=r'$\operatorname{sinc}(t)$')
    ax.scatter(integers, np.sinc(integers), color='red',
               s=16, zorder=3, label='Integer values')
    ax.set(
        title='Normalized Sinc Function',
        xlabel='$t$',
        ylabel=r'$\operatorname{sinc}(t)$',
        xlim=(-4, 4),
    )
    ax.grid(alpha=0.3)
    add_legend(ax)
    plt.show()

    # Plot the shifted sinc functions and their sum
    x_rec = sinc_reconstruction(x, t)

    ax = create_axes()
    for k, value in enumerate(x):
        ax.plot(
            t, value * np.sinc(t - k), linewidth=0.8,
            label=rf'$x({k})\operatorname{{sinc}}(t-{k})$',
        )

    ax.plot(t, x_rec, color='black', linewidth=2,
            label=r'$f_{\mathrm{rec}}(t)$')
    ax.scatter(n, x, color='red', s=20, zorder=3,
               label='Samples')
    ax.set(
        title='Reconstruction from Shifted Sinc Functions',
        xlabel='$t$',
        ylabel='Signal value',
        xlim=(-2, 6),
    )
    ax.grid(alpha=0.3)
    add_legend(ax)
    plt.show()

    # Verify interpolation at the sample positions
    # x_at_samples = sinc_reconstruction(x, n)
    # error = np.max(np.abs(x_at_samples - x))
    # print(f'Maximum error at sample positions: {error:.2e}')

    # Change one sample and compare the reconstructions
    x_modified = x.copy()
    x_modified[2] = 0.5
    x_rec_modified = sinc_reconstruction(x_modified, t)

    ax = create_axes()
    ax.plot(t, x_rec, color='black',
            label='Original reconstruction')
    ax.plot(t, x_rec_modified, color='blue',
            label='Modified reconstruction')
    ax.scatter(n, x_modified, color='red', s=20, zorder=3,
               label='Samples')
    ax.scatter(n[2], x_modified[2], color='red', edgecolor='black',
               linewidth=1.2, s=55, zorder=4,
               label='Modified sample')
    ax.set(
        title='Effect of Changing One Sample',
        xlabel='$t$',
        ylabel='Signal value',
        xlim=(-2, 6),
    )
    ax.grid(alpha=0.3)
    add_legend(ax)
    plt.show()
    
def exercise_sound_design(show_result=True):
    """Exercise 3: Synthesizing a Plucked-String Sound."""
    if not show_result:
        return

    def synthesize_plucked_string(
            dur=2, silence=0.25, freq=220,
            harmonics=(1, 0.4, 0.2, 0.1, 0.05),
            attack=0.01, release=0.3, decay=1.5,
            noise_amp=0.02, noise_dur=0.03,
            sr=16000, seed=0):
        """Synthesize a plucked-string sound."""
        if attack + release > dur:
            raise ValueError('Attack and release must fit within the note.')
        if noise_dur > dur:
            raise ValueError('The noise transient must fit within the note.')
        if len(harmonics) * freq >= sr / 2:
            raise ValueError(
                'A harmonic reaches or exceeds the Nyquist frequency.'
            )

        t_sound = np.arange(int(dur * sr)) / sr

        # Add the fundamental and its harmonics
        x = sum(
            amp * np.sin(2 * np.pi * k * freq * t_sound)
            for k, amp in enumerate(harmonics, start=1)
        )

        # Create the attack, gradual decay, and release
        envelope = np.exp(-decay * t_sound)
        n_attack = max(1, int(attack * sr))
        n_release = max(1, int(release * sr))
        envelope[:n_attack] *= np.linspace(0, 1, n_attack)
        envelope[-n_release:] *= np.linspace(1, 0, n_release)
        x *= envelope

        # Add a short noise transient
        rng = np.random.default_rng(seed)
        n_noise = max(1, int(noise_dur * sr))
        x[:n_noise] += (
            noise_amp * rng.standard_normal(n_noise)
            * np.linspace(1, 0, n_noise)
        )

        # Add initial silence
        n_silence = int(silence * sr)
        x = np.concatenate((np.zeros(n_silence), x))
        envelope = np.concatenate((np.zeros(n_silence), envelope))
        t = np.arange(len(x)) / sr

        # Prevent clipping
        peak = np.max(np.abs(x))
        if peak > 1:
            x *= 0.9 / peak

        return x, t, envelope, sr

    dur, silence, freq, sr = 2, 0.25, 220, 16000

    sounds = {
        'Warm A3': dict(
            harmonics=(1, 0.3, 0.12, 0.06, 0.03),
            attack=0.02, release=0.5, decay=1.2,
            noise_amp=0.01, noise_dur=0.02,
        ),
        'Bright A3': dict(
            harmonics=(1, 0.7, 0.5, 0.35, 0.25, 0.18, 0.12, 0.08),
            attack=0.005, release=0.25, decay=2,
            noise_amp=0.05, noise_dur=0.04,
        ),
    }

    for label, parameters in sounds.items():
        x, t, envelope, _ = synthesize_plucked_string(
            dur=dur, silence=silence, freq=freq, sr=sr, **parameters
        )

        attack = parameters['attack']
        release = parameters['release']
        onset = silence
        attack_end = onset + attack
        release_start = onset + dur - release
        signal_end = onset + dur
        n_harmonics = len(parameters['harmonics'])

        fig, axes = plt.subplots(
            2, 1, figsize=(6.2, 2.8), layout='tight', sharex=True
        )

        # Synthesized waveform
        axes[0].plot(t, x, color='black', linewidth=0.7,
                     label='Synthesized signal')
        axes[0].set_title(
            rf'{label}: $f_0={freq}$ Hz, {n_harmonics} harmonics'
        )
        axes[0].set_ylabel('Signal value')
        axes[0].legend(loc='upper right', fontsize=7, framealpha=1)

        # Envelope and its phases
        axes[1].plot(t, envelope, color='blue', linewidth=1.5,
                     label='Envelope')
        axes[1].axvspan(0, onset, color='gray', alpha=0.15,
                        label='Silence')
        axes[1].axvspan(onset, attack_end, color='green', alpha=0.2,
                        label=rf'Attack ({attack:g} s)')
        axes[1].axvspan(
            attack_end, release_start, color='blue', alpha=0.06,
            label='Decay / sustain'
        )
        axes[1].axvspan(
            release_start, signal_end, color='orange', alpha=0.2,
            label=rf'Release ({release:g} s)'
        )
        axes[1].set_xlabel('Time (seconds)')
        axes[1].set_ylabel('Envelope')
        axes[1].legend(
            loc='upper right', fontsize=7, framealpha=1, ncol=2
        )

        for ax in axes:
            ax.set_xlim(0, signal_end)
            ax.grid(alpha=0.3)

        plt.show()
        print(label)
        ipd.display(ipd.Audio(x, rate=sr, normalize=False))
