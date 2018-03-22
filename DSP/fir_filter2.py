import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import firwin, freqz, lfilter
from plot_mfreqz_impz import mfreqz, impz

#A low pass filter
n = 101
a = firwin(n, cutoff=0.3, window="hamming")
#Frequency and phase response
mfreqz(a)
#Impulse and step response
impz(a)
#plt.show()

#A high pass filter
n = 101
a = firwin(n, cutoff=0.3, window="hanning")
#Spectral inversion
a = -a
a[n // 2] = a[n // 2] + 1
mfreqz(a)
impz(a)
#plt.show()

#A band pass filter
n = 1001
#Lowpass filter
a = firwin(n, cutoff=0.3, window='blackmanharris')
#Highpass filter with spectral inversion
b = -firwin(
    n, cutoff=0.5, window='blackmanharris')
b[n // 2] = b[n // 2] + 1
#Combine into a bandpass filter
d = -(a + b)
d[n // 2] = d[n // 2] + 1
#Frequency response
mfreqz(d)
impz(d)

plt.show()
