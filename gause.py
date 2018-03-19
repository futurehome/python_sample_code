#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import re

mu, sigma = 0, .1
s = np.random.normal(loc=mu, scale=sigma, size=1000)

count, bins, _ = plt.hist(s, 30, normed=True)
        # normed是进行拟合的关键
        # count统计某一bin出现的次数，在Normed为True时，可能其值会略有不同
plt.plot(bins, 1./(np.sqrt(2*np.pi)*sigma)*np.exp(-(bins-mu)**2/(2*sigma**2)), lw=2, c='r')
plt.show()