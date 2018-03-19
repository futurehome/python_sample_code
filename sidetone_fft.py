#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#x = np.linspace(0, 20, 100)
#plt.plot(x, np.sin(x))
#plt.show()

# 1 second of data samples at spacing of 1/1000 seconds
#t = np.arange(0, 1, 1.0/1000)
# sine wave of 100 Hz
#s = np.sin(2 * np.pi * 100 * t)
s = np.loadtxt('sidetone.txt')
# plot first 20 points of the resulting data (why not all 1000?)
#plt.plot(s[:20])
#plt.show()

#noise_amp = 1.0
# Another signal with two sine waves
#s = np.sin(2*np.pi*100*t)+np.sin(2*np.pi*200*t)
#s = np.sin(2*np.pi*100*t)+np.sin(2*np.pi*200*t)+noise_amp * np.random.randn(len(t))
# Note: you may need to use fft.fft is you are using ipython
ft = np.fft.fft(s)/len(s)
#plt.plot(20*np.log10(abs(ft)))
plt.semilogx(20*np.log10(abs(ft)))
#plt.loglog(abs(ft))
plt.show()


#from scipy.signal import remez
#lpf = remez(21, [0, 0.2, 0.3, 0.5], [1.0, 0.0])
#from scipy.signal import freqz
#w, h = freqz(lpf)
#plt.plot(w/(2*np.pi), 20*np.log10(abs(h)))
#plt.show()

#from scipy.signal import lfilter
#sout = lfilter(lpf, 1, s)
#plt.plot(20*np.log10(abs(np.fft.fft(s))))
#plt.plot(20*np.log10(abs(np.fft.fft(sout))))
#plt.show()