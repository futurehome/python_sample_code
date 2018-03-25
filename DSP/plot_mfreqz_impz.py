import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import MultiCursor
from scipy.signal import freqz, lfilter


def mfreqz(b, a=1, **kwargs):
    '''
    Plot frequency and phase response
    Parameters in **kwargs: SampleRate=np.pi/2, PassBandStart=0, PassBandStop=0, PassBandRipple=0, 
    PassBandEdge=0, StopBandEdge=0, StopBandAttenu=0
    '''
    SampleRate = np.pi/2
    for key in kwargs:
        if key == 'SampleRate': 
            SampleRate = kwargs[key] 


    w, h = freqz(b, a)
    w_hz = w * SampleRate * 2 / np.pi
    h_dB = 20 * np.log10(abs(h) / max(h))
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(w_hz, h_dB)
    #
    #Plot lines for dB=0 and dB=-3 cutoff
    #
    ax1.axhline(y=0, ls='--', lw=0.5, color='r')
    ax1.axhline(y=-3, ls='--', lw=0.5, color='r')
    #
    #Plot lines for different parameters
    #
    for key in kwargs:
        if key == 'PassBandStart':
            ax1.axvline(kwargs[key], color='r', ls='--', lw=0.5)
        if key == 'PassBandStop':
            ax1.axvline(kwargs[key], color='r', ls='--', lw=0.5)
            PassBandStop = kwargs[key]
        if key == 'PassBandRipple':
            ax1.axhline(y=-2*kwargs[key], color='r', ls='--', lw=0.5)
            #ax1.annotate('Pass Band Ripple', xy=(0, -2*PassBandRipple-4), color='r')
        if key == 'PassBandEdge':
            ax1.axvline(kwargs[key], color='r', ls='--', lw=0.5)
            PassBandEdge = kwargs[key]
        if key == 'StopBandEdgeBandPass':
            ax1.axvline(kwargs[key], color='r', ls='--', lw=0.5)
        if key == 'StopBandEdge':
            ax1.axvline(kwargs[key], color='r', ls='--', lw=0.5)
            StopBandEdge = kwargs[key]
        if key == 'StopBandAttenu':
            ax1.axhline(-kwargs[key], color='r', ls='--', lw=0.5)
            StopBandAttenu = kwargs[key]
    #ax1.annotate('Pass Band Ripple', xy=(0, -2*PassBandRipple-4), color='r')
    ax1.set_ylabel('Magnitude (db)')
    #ax1.set_xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_title(r'Frequency response')

    axzoomup = fig.add_axes([0.15, 0.77, 0.25, 0.1])
    axzoomup.set_xlim(PassBandStop-50000, PassBandEdge+10000)
    axzoomup.set_ylim(-5, 1)
    axzoomup.plot(w_hz, h_dB)
    axzoomup.axhline(y=0, ls='--', lw=0.5, color='r')
    axzoomup.axhline(y=-3, ls='--', lw=0.5, color='r')
    for key in kwargs:
        if key == 'PassBandStart':
            axzoomup.axvline(kwargs[key], color='r', ls='--', lw=0.5)
        if key == 'PassBandStop':
            axzoomup.axvline(kwargs[key], color='r', ls='--', lw=0.5)
        if key == 'PassBandRipple':
            axzoomup.axhline(y=-2*kwargs[key], color='r', ls='--', lw=0.5)
            #ax1.annotate('Pass Band Ripple', xy=(0, -2*PassBandRipple-4), color='r')
        if key == 'PassBandEdge':
            axzoomup.axvline(kwargs[key], color='r', ls='--', lw=0.5)
        if key == 'StopBandEdgeBandPass':
            axzoomup.axvline(kwargs[key], color='r', ls='--', lw=0.5)
        if key == 'StopBandEdge':
            axzoomup.axvline(kwargs[key], color='r', ls='--', lw=0.5)
        if key == 'StopBandAttenu':
            axzoomup.axhline(-kwargs[key], color='r', ls='--', lw=0.5)

    axzoomdn = fig.add_axes([0.15, 0.64, 0.25, 0.1])
    axzoomdn.set_xlim(StopBandEdge-10000, StopBandEdge+50000)
    axzoomdn.set_ylim(-StopBandAttenu-100, -StopBandAttenu+50)
    axzoomdn.plot(w_hz, h_dB)
    for key in kwargs:
        if key == 'PassBandStart':
            axzoomdn.axvline(kwargs[key], color='r', ls='--', lw=0.5)
        if key == 'PassBandStop':
            axzoomdn.axvline(kwargs[key], color='r', ls='--', lw=0.5)
        if key == 'PassBandRipple':
            axzoomdn.axhline(y=-2*kwargs[key], color='r', ls='--', lw=0.5)
            #ax1.annotate('Pass Band Ripple', xy=(0, -2*PassBandRipple-4), color='r')
        if key == 'PassBandEdge':
            axzoomdn.axvline(kwargs[key], color='r', ls='--', lw=0.5)
        if key == 'StopBandEdgeBandPass':
            axzoomdn.axvline(kwargs[key], color='r', ls='--', lw=0.5)
        if key == 'StopBandEdge':
            axzoomdn.axvline(kwargs[key], color='r', ls='--', lw=0.5)
        if key == 'StopBandAttenu':
            axzoomdn.axhline(-kwargs[key], color='r', ls='--', lw=0.5)

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

    plt.tight_layout()
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
