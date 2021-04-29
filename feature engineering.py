# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:49:25 2021

@author: DELL
"""

import numpy as np
import statistics
import matplotlib.pyplot as plt
from scipy import stats
import math
import statsmodels.api as sm

data = np.random.normal(0,1,100)


class toan2:
    def __init__(self):
       self.data = data
       self.mean = statistics.mean(self.data)
       self.min = np.min(self.data)
       self.max = np.max(self.data)
       self.med = statistics.median(self.data)
       self.per1 = np.percentile(self.data, 25)
       self.per2 = np.percentile(self.data, 75)
       self.mode = statistics.mode(self.data)
       self.quantile = np.quantile(self.data, 0.02)
       
    def hist(self):
        plt.hist(self.data, density=2, color = 'yellow')
        mu = 0
        sigma = math.sqrt(np.std(self.data))
        x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
        plt.plot(x, stats.norm.pdf(x, mu, sigma), color = 'red')
        return plt.show()

    
    def qq_plot(self):
        sm.qqplot(data, line ='45', color = 'green')
        plt.show()

BT = toan2()
print(data)
print('Gia tri trung binh',BT.mean())
print('Gia tri trung vi la',BT.med())
print('Gia tri max la: ', BT.max())
print('Gia tri min la: ', BT.min())
print('Gia tri phuong sai la',BT.std())
print('Bach phan vi la',BT.percentile())
print('Gia tri mode la',BT.mode())
print('Tu phan vi la', BT.quantiles())


print(BT.hist())
print(BT.qq_plot())