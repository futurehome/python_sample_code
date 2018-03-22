import scipy as sp
from scipy import signal
import pylab as pl



def gauss_kern(size, sizey=None):
    """ Returns a normalized 2D gauss kernel array for convolutions """
    size = int(size)
    if not sizey:
        sizey = size
    else:
        sizey = int(sizey)
    x, y = sp.mgrid[-size:size + 1, -sizey:sizey + 1]
    g = sp.exp(-(x**2 / float(size) + y**2 / float(sizey)))
    return g / g.sum()


def blur_image(im, n, ny=None):
    """ blurs the image by convolving with a gaussian kernel of typical
        size n. The optional keyword argument ny allows for a different
        size in the y direction.
    """
    g = gauss_kern(n, sizey=ny)
    improc = signal.convolve(im, g, mode='valid')
    return improc


X, Y = sp.mgrid[-70:70, -70:70]
Z = sp.cos((X**2 + Y**2) / 200.) + sp.random.normal(size=X.shape)
pl.figure()
pl.imshow(Z)

Z2 = blur_image(Z, 3)
pl.figure()
pl.imshow(Z2)

pl.show()