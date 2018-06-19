# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 09:41:50 2018

@author: bob
"""

import pandas as pd
import numpy as np 
import csv
score = pd.read_csv('score_final_test.txt', names=['id', 'faculty', 'ranks'])
dataset = score[['id', 'faculty', 'ranks']].values

sort_array = dataset[np.lexsort(dataset[:,::-1].T)]     

with open('result.txt', 'w') as f:
    for student in sort_array:
        stuid = student[0]
        faculty = student[1]
        rank = student[2]
        row = [stuid, faculty, rank]
    

        writer=csv.writer(f)
        writer.writerow(row)