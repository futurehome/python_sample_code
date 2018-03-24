import matplotlib.pyplot as plt
from scipy.signal import iirdesign
from plot_mfreqz_impz import mfreqz, impz
import numpy as np

#A low pass filter
b,a = iirdesign(wp = [0.05, 0.3], ws= [0.02, 0.35], gstop= 60, gpass=1, ftype='ellip')
#Frequency and phase response
#mfreqz(b, a)
SampleRate = 192000
rate = SampleRate / (2 * np.pi)
mfreqz(b, a, 
    SampleRate=192000, 
    PassBandStart=0.05*rate,
    PassBandStop=0.3*rate,
    PassBandRipple=1, 
    StopBandEdgeBandPass=0.02*rate,
    StopBandEdge=0.35*rate,
    StopBandAttenu=60)
#Impulse and step response
#impz(b, a)

plt.show()
