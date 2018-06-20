# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 23:43:02 2018

@author: bob
"""

import matplotlib.pyplot as plt
import pandas as pd

X = pd.read_csv('X_train.csv')
x = X[X['labels'] == 0]['DormweekendTimes']
y = X[X['labels'] == 0]['libraryweekendTimes']
target = X['labels'].values
species = target

plt.figure()
plt.scatter(x, y, c=['b', 'r'], linewidths=0.1, marker='.')
plt.show()

