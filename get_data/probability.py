# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:36:48 2018

@author: bob
"""
import readFromFile

'''
seaching the prediction with stu_id in probability.txt
return the float prediction value
'''
def prediction(stu_id):
    path = 'data/probability.txt'
    lines = readFromFile.readLines(path)
    for line in lines:
        s_id = int(line.split(',')[0])
        prediction = float(line.split(',')[1])    
        if stu_id == s_id:
            #print s_id, prediction
            return prediction

        
        