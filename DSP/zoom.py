import matplotlib.pyplot as plt
import numpy as np

def zoom():
    figsrc, axsrc= plt.subplots(nrows=2, ncols=1)
    figzoom, axzoom = plt.subplots()
    axsrc[0].set(xlim=(0, 1), ylim=(0, 1), autoscale_on=False,
              title='Click to zoom')
    axsrc[1].set(xlim=(0, 1), ylim=(0, 1), autoscale_on=False,
              title='Click to zoom')
    axzoom.set(xlim=(0.45, 0.55), ylim=(0.4, 0.6), autoscale_on=False,
               title='Zoom window')

    x, y, s, c = np.random.rand(4, 200)
    s *= 200

    axsrc[0].plot(s, c)
    axsrc[1].plot(x, y)
    axzoom.scatter(x, y, s, c)


    def onpress(event):
        if event.button != 1:
            return
        x, y = event.xdata, event.ydata
        axzoom.set_xlim(x - 0.1, x + 0.1)
        axzoom.set_ylim(y - 0.1, y + 0.1)
        figzoom.canvas.draw()

    figsrc.canvas.mpl_connect('button_press_event', onpress)
    plt.show()

zoom()