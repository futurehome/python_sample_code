import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import MultiCursor
from scipy.signal import freqz, lfilter


def mfreqz(b, a=1, SampleRate=np.pi/2, PassBandStart=0, PassBandStop=0, PassBandRipple=0, 
    PassBandEdge=0, StopBandEdge=0, StopBandAttenu=0):
    '''
    Plot frequency and phase response
    '''
    w, h = freqz(b, a)
    w_hz = w * SampleRate * 2 / np.pi
    h_dB = 20 * np.log10(abs(h) / max(h))
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(w_hz, h_dB)
    #for p in [
    #    patches.Rectangle(
    #        (PassBandStart, -2*PassBandRipple),
    #        (PassBandStop-PassBandStart),
    #        2*PassBandRipple,
    #        hatch='.',
    #        fill=False,
    #        color='r',
    #        ls='--',
    #        lw=1),
    #]:
    #    ax1.add_patch(p)
    ax1.axhline(y=0, ls='--', lw=0.5, color='r')
    ax1.axhline(y=-2*PassBandRipple, ls='--', lw=0.5, color='r')
    #ax1.annotate('Pass Band Ripple', xy=(0, -2*PassBandRipple-4), color='r')
    ax1.axhline(y=-3, ls='--', lw=0.5, color='r')
    #ax1.hlines(0, 0, PassBandEdge, color='r', linestyle='--', linewidth=0.5)
    #ax1.hlines(-2*PassBandRipple, 0, PassBandEdge, color='r', linestyle='--', linewidth=0.5)
    ax1.axvline(PassBandStop, color='r', linestyle='--', lw=0.5)
    ax1.axvline(PassBandEdge, color='r', linestyle='--', lw=0.5)
    ax1.axvline(StopBandEdge, color='r', linestyle='--', lw=0.5)
    ax1.axhline(-StopBandAttenu, color='r', linestyle='--', lw=0.5)
    #plt.plot(w / max(w), h_dB)
    #plt.ylim(-150, 205)
    ax1.set_ylabel('Magnitude (db)')
    #ax1.set_xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_title(r'Frequency response')

    ax2 = fig.add_subplot(212, sharex=ax1)
    h_Phase = np.unwrap(np.arctan2(np.imag(h), np.real(h)))
    ax2.plot(w_hz, h_Phase)
    #plt.plot(w / max(w), h_Phase)
    ax2.set_ylabel('Phase (radians)')
    #ax2.set_xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_title(r'Phase response')
    plt.subplots_adjust(hspace=0.5)
    _ = MultiCursor(fig.canvas, (ax1, ax2), color='r', lw=1)
    plt.show()


def impz(b, a=1):
    '''
    Plot step and impulse response
    '''
    l = len(b)
    impulse = np.repeat(0., l)
    impulse[0] = 1.
    x = np.arange(0, l)
    response = lfilter(b, a, impulse)
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.stem(x, response)
    ax1.set_ylabel('Amplitude')
    ax1.set_xlabel(r'n (samples)')
    ax1.set_title(r'Impulse response')

    ax2 = fig.add_subplot(212)
    step = np.cumsum(response)
    ax2.stem(x, step)
    ax2.set_ylabel('Amplitude')
    ax2.set_xlabel(r'n (samples)')
    ax2.set_title(r'Step response')
    plt.subplots_adjust(hspace=0.5)
    _ = MultiCursor(fig.canvas, (ax1, ax2), color='r', lw=1)
    plt.show()
