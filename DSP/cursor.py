from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(211, facecolor='#FFFFCC')
ax2 = fig.add_subplot(212, facecolor='#FFFFCC')

x, y = 4*(np.random.rand(2, 100) - .5)
ax1.plot(x, y, 'o')
ax2.plot(x, y, 'o')

# set useblit = True on gtkagg for enhanced performance
cursor1 = Cursor(ax1, useblit=True, color='red', linewidth=1)
cursor2 = Cursor(ax2, useblit=True, color='red', linewidth=1)

plt.show()