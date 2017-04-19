# @Author: Shane Yu  @Date created: April 17, 2017
import matplotlib
matplotlib.use('Agg') # server的backend display參數設定，否則無法使用pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame as df


class BreastCancerAnalysis(object):
    def __init__(self):
        self.dataPath = './data.txt'


    def getData(self):
        data = pd.read_csv(self.dataPath, header=None) # header 加第一行標頭
        return data


    def createBoxPlot(self, data):
        plt.figure(figsize=(10,10), dpi=150)
        data[[1,2]].boxplot()
        plt.legend(loc='best')
        plt.savefig('./result/Box.png', dpi=150, format='png')


    def createHistogram(self, data):
        plt.figure(figsize=(10,10), dpi=150)
        plt.hist(data[[1,2]])
        plt.legend(loc='best')
        plt.savefig('./result/Histagram.png', dpi=150, format='png')


    def createPlot(self, data):
        plt.figure(figsize=(40,10), dpi=150)
        plt.plot(data[[1,2]])
        plt.legend(loc='best')
        plt.savefig('./result/Plot.png', dpi=150, format='png')


    def pearsonColorPlot(self, data):
        plt.figure(figsize=(10,10), dpi=150)
        correlation = data.corr()
        correMatrix= df(correlation)
        plt.pcolor(correMatrix)
        plt.legend(loc='best')
        plt.savefig('./result/Pcolor.png', dpi=150, format='png')


    def createScatterPlot(self, data):
        plt.figure(figsize=(10,10), dpi=150)
        plt.scatter(data.loc[data[10] == 2][1], data.loc[data[10] == 2][2], c='green', s=20, label='2', alpha=0.8, edgecolors='white')
        plt.scatter(data.loc[data[10] == 4][1], data.loc[data[10] == 4][2], c='red', s=20, label='4', alpha=0.8, edgecolors='white')
        plt.legend(loc='best')
        plt.savefig('./result/Scatter.png', dpi=150, format='png')


    def exec(self):
        PDData = self.getData()
        self.createBoxPlot(PDData)
        self.createHistogram(PDData)
        self.createPlot(PDData)
        self.pearsonColorPlot(PDData)
        self.createScatterPlot(PDData)



if __name__ == '__main__':
    obj = BreastCancerAnalysis()
    obj.exec()
