#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 22:50:33 2018

@author: hadoop
"""

import pandas as pd
import numpy as np
def getXtrain():
    borrow = pd.read_csv('../data/test/borrow.csv', names=['stuId', 'ifBorrowed', 'numOfBorrowed'],
                         dtype=np.float)
    card = pd.read_csv('../data/test/card.csv', names=['stuId', 'library', 'hospital', 'market', 'water', 'canteen', 'washer',
                    'other', 'academic_office', 'printing', 'bus', 'shower'],
                         dtype=np.float)
    dorm = pd.read_csv('../data/test/dorm.csv', names=['stuId', 'DormtimesPerDay', 'DormtotalDays','DormweekendTimes'],
                         dtype=np.float)
    library = pd.read_csv('../data/test/library.csv', names=['stuId', 'librarytotalDays', 'libraryweekendTimes', 'librarytotalcol_nameTimes'],
                         dtype=np.float)
    rank = pd.read_csv('../data/test/rank.txt', names=['stuId', 'ranks'],
                         dtype=np.float)
    
    X_borrow = pd.merge(card, borrow, how='left', on='stuId')
    X_dorm = pd.merge(X_borrow, dorm, how='left', on='stuId')
    X_library = pd.merge(X_dorm, library, how='left', on='stuId')
    X_rank = pd.merge(X_library, rank, how='left', on='stuId')

#X_train = pd.read_csv('../data/test/X_train.csv', dtype=np.float)
#labels = pd.read_csv('../data/train/labels.csv', dtype=np.float)
#X = pd.merge(X_train, labels, how='left', on='stuId')
