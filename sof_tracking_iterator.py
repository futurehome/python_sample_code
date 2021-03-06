#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy.stats as st
import re


class Data:
    '''The data generated by sof tracking'''
    rules_filename = 'data_captured.dat'

    def __init__(self):
        self.data_file = open(self.rules_filename, 'rb')

    def __iter__(self):
        return self

    def __next__(self):
        if self.data_file.closed:
            raise StopIteration
        dw = self.data_file.read(4)
        if not dw:
            self.data_file.close()
            raise StopIteration
        data = (int.from_bytes(dw[1:4], byteorder='big', signed=True))
        return data


if __name__ == '__main__':
    plot_point = []
    for plot_data in Data():
        plot_point.append(plot_data)
    plt.plot(plot_point)
    plt.show()
