#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:13:17 2018

@author: Bomiro
"""
import pandas as pd
import matplotlib.pyplot as plt

card = pd.read_csv('draw_card.csv')
dorm = pd.read_csv('draw_dorm.csv', names=[
 'stuId',
 '01_00exitDiv',
 '01_00enterDiv',
 '03_00exitDiv',
 '03_00enterDiv',
 '06_00exitDiv',
 '06_00enterDiv',
 '09_00exitDiv',
 '09_00enterDiv',
 '12_50exitDiv',
 '12_50enterDiv',
 '11_20exitDiv',
 '11_20enterDiv',
 '16_50exitDiv',
 '16_50enterDiv',
 '19_00exitDiv',
 '19_00enterDiv',
 '22_00exitDiv',
 '22_00enterDiv',
 'weekendTimesDiv',
 'timesPerDay'])

draw = pd.merge(card, dorm, how='right', on='stuId')
draw = draw.drop(['timesPerDay'], axis=1)

cols = list(draw.columns)[1:]
x = draw.ix[450].drop('stuId')
plt.title("Infomation of Single Student")
plt.xlabel("Items")
plt.ylabel("Percentage")
plt.ylim(-0.1,1.1)
plt.xticks(rotation=90)
plt.scatter(cols, x)
plt.show()