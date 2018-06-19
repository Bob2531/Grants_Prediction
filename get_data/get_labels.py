#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:19:19 2018

@author: hadoop
"""

import pandas as pd
import numpy as np

labels = pd.read_csv('../data/subsidy_train.txt')
for index, row in labels.iterrows():
    if row['subsidy'] == 0:
        row['subsidy'] = 0
    if row['subsidy'] == 1000:
        row['subsidy'] = 1
    if row['subsidy'] == 1500:
        row['subsidy'] = 2
    if row['subsidy'] == 2000:
        row['subsidy'] = 3
    labels.ix[index] = row
labels.to_csv('../data/labels.csv', index=False)