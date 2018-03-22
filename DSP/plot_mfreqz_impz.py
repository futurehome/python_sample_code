import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import freqz, lfilter


def mfreqz(b, a=1):
    '''
    Plot frequency and phase response
    '''
    w, h = freqz(b, a)
    h_dB = 20 * np.log10(abs(h))
    plt.figure()
    plt.subplot(211)
    plt.plot(w / max(w), h_dB)
    plt.ylim(-150, 5)
    plt.ylabel('Magnitude (db)')
    plt.xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    plt.title(r'Frequency response')
    plt.subplot(212)
    h_Phase = np.unwrap(np.arctan2(np.imag(h), np.real(h)))
    plt.plot(w / max(w), h_Phase)
    plt.ylabel('Phase (radians)')
    plt.xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    plt.title(r'Phase response')
    plt.subplots_adjust(hspace=0.5)


def impz(b, a=1):
    '''
    Plot step and impulse response
    '''
    l = len(b)
    impulse = np.repeat(0., l)
    impulse[0] = 1.
    x = np.arange(0, l)
    response = lfilter(b, a, impulse)
    plt.figure()
    plt.subplot(211)
    plt.stem(x, response)
    plt.ylabel('Amplitude')
    plt.xlabel(r'n (samples)')
    plt.title(r'Impulse response')
    plt.subplot(212)
    step = np.cumsum(response)
    plt.stem(x, step)
    plt.ylabel('Amplitude')
    plt.xlabel(r'n (samples)')
    plt.title(r'Step response')
    plt.subplots_adjust(hspace=0.5)
