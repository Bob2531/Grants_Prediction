#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 21:20:59 2018

@author: hadoop
"""

import numpy as np


def get_score_data(stu_id):
    with open('data/score_train.txt', 'r') as f:
        lines = f.readlines()
        stu_rank = 0
        stu_faculty = 0
        for line in lines:
            info = line.strip().split(',')
            if stu_id == int(info[0]):
                stu_rank = int(info[2])
                stu_faculty = int(info[1])
                print "id is: %s \nfaculty is: %s \nrank is: %s" \
                    %(stu_id, stu_faculty, stu_rank)
                break
        faculty_rank = []
        for line in lines:
            info = line.strip().split(',')
            if stu_faculty == int(info[1]):
                faculty_rank.append(int(info[2]))
                #print info
        np_arr = np.array(faculty_rank)
        #print faculty_rank
        max_rank = 0
        try:
            max_rank = np_arr.max()
        except ValueError:  #raised if `y` is empty.
            print "array is empty"
        print "faculty'max rank is: ", max_rank
        re_rank = []
        re_rank.append(stu_rank)
        re_rank.append(max_rank)
    return re_rank

#a, b = get_score_data(0)    
#print a, b
