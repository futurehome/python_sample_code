#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy.stats as st
import re

with open('data_captured.dat', 'rb') as f:
    #    hex = ""
    #    for byte in f.read():
    #        hex += "{0:02x}".format(byte)
    #
    #    pattern = re.compile(r'((00)(..){3}){4}')
    #    result = pattern.search(hex)
    #
    #    f.seek(result.span()[0]//2)
    dw = f.read(4)
    data = []
    while dw:
        data.append(int.from_bytes(dw[1:4], byteorder='big', signed=True))
        dw = f.read(4)

    #myarray = np.asarray(dw)
    #mu, sigma = 0, 0.1
    #count, bins, _ = plt.hist(myarray, normed=True)
    #plt.plot(bins, 1./(np.sqrt(2*np.pi)*sigma)*np.exp(-(bins-mu)**2/(2*sigma**2)), lw=2, c='r')
    #s_fit = np.linspace(min(data), max(data))
    #plt.plot(s_fit, st.norm(mu, sigma).pdf(s_fit), lw=2, c='r')
    plt.plot(data)
    plt.show()

#pattern = '''
#    ^                   #begin of the string
#    ('\x00')              #first should be 00 or aa
#    #('\x'..){3}           #3 any other bytes
#    $
#    '''

#s = np.loadtxt('data_captured.dat')
# plot first 20 points of the resulting data (why not all 1000?)
#plt.plot(s[:20])
#plt.show()

#from scipy.signal import lfilter
#sout = lfilter(lpf, 1, s)
#plt.plot(20*np.log10(abs(np.fft.fft(s))))
#plt.plot(20*np.log10(abs(np.fft.fft(sout))))
#plt.show()