# @Author: Shane Yu  @Date created: June 6, 2017
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame as df

class PlotHistogram(object):
    def __init__(self):
        self.dataPath = './data.csv'

    def preprocessing(self):
        data = pd.read_csv(self.dataPath)
        ageCol = data[[5]].fillna(data[[5]].mean())
        # self.createHistogram(ageCol['Age'].values.tolist())
        self.createHistogram(ageCol['Age'])

    def createHistogram(self, data):
        plt.hist(data, histtype='bar', rwidth=0.8, color='green')
        plt.savefig('Histogram.png', dpi=150, format='png')

if __name__ == '__main__':
    obj = PlotHistogram()
    obj.preprocessing()
