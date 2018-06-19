# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 05:56:15 2018

@author: bob
"""

'''
parameter: list
change value in list to .2f
return new format list
'''
def change(values):
    new_values = []
    for value in values:
        new_value = round(value, 2)
        new_values.append(new_value)
    return new_values
    
'''
parameter: a dict
func: separate a dict into tow list
return tow list which are labels_list and values_list
'''
def separate(dic):
    labels = []#define labels with list
    values = []#define values with list
    for label, value in dic.iteritems():
        labels.append(label)
        values.append(value)
    values = change(values)
    return labels, values