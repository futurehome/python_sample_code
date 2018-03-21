import numpy


def smooth(x, window_len=11, window='hanning'):
    """smooth the data using a window with requested size.
    
    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal 
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.
    
    input:
        x: the input signal 
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal
        
    example:

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)
    
    see also: 
    
    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
    scipy.signal.lfilter
 
    TODO: the window parameter could be the window itself if an array instead of a string
    NOTE: length(output) != length(input), to correct this: return y[(window_len/2-1):-(window_len/2)] instead of just y.
    """

    if x.ndim != 1:
        raise ValueError("smooth only accepts 1 dimension arrays.")

    if x.size < window_len:
        raise ValueError("Input vector needs to be bigger than window size.")

    if window_len < 3:
        return x

    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError(
            "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"
        )

    s = numpy.r_[x[window_len - 1:0:-1], x, x[-2:-window_len - 1:-1]]
    #print(len(s))
    if window == 'flat':  #moving average
        w = numpy.ones(window_len, 'd')
    else:
        w = eval('numpy.' + window + '(window_len)')

    y = numpy.convolve(w / w.sum(), s, mode='valid')
    return y


import numpy as np
import pylab as pl


def smooth_demo():

    t = np.linspace(-4, 4, 100)
    x = np.sin(t)
    xn = x + pl.randn(len(t)) * 0.1
    #_ = smooth(x)

    ws = 31

    pl.subplot(211)
    pl.plot(pl.ones(ws))

    windows = ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']

    #hold(True)
    for w in windows[1:]:
        eval('pl.plot(np.' + w + '(ws) )')

    pl.axis([0, 30, 0, 1.1])

    pl.legend(windows)
    pl.title("The smoothing windows")

    pl.subplot(212)
    pl.plot(x)
    pl.plot(xn)
    for w in windows:
        pl.plot(smooth(xn, 10, w))
    l = ['original signal', 'signal with noise']
    l.extend(windows)

    pl.legend(l)
    pl.title("Smoothing a noisy signal")
    pl.show()


if __name__ == '__main__':
    smooth_demo()