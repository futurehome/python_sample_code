import matplotlib.pyplot as plt
from scipy.signal import iirdesign
from plot_mfreqz_impz import mfreqz, impz

#A low pass filter
b,a = iirdesign(wp = [0.05, 0.3], ws= [0.02, 0.35], gstop= 60, gpass=1, ftype='ellip')
#Frequency and phase response
mfreqz(b, a)
#Impulse and step response
impz(b, a)

plt.show()
