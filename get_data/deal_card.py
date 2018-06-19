#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:30:16 2017

@author: hadoop
"""

import pandas as pd
column = ['ID','Consumption','Location','Ways','DataTime','Sum','Balance']

with open('../data/test/card_final_test.txt','r') as file:
    card = pd.read_csv(file, names=column)
    card = card.drop_duplicates()

for ID, group in card.groupby('ID'):
    file_name = '../data/card_test/' + str(ID) + '.csv'
    print file_name
    group.to_csv(file_name, index=False, header=False)
    #print group