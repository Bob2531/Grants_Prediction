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