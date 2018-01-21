#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 21:20:59 2018

@author: hadoop
"""



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
        faculty_rank.sort()
        try:
            max_rank = faculty_rank[-1]
            return_list = [stu_rank, max_rank]
        except IndexError:
            print "empty faculty_list"
            max_rank = 0
            return_list = [stu_rank, max_rank]
                
    return return_list
'''
a, b= get_score_data(22)    
print a, b
'''


        