#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 21:20:59 2018

@author: hadoop
"""
import os
import csv

def get_score_data(stu_id):
    score_train = '../data/train/score_train.txt'
    score_test = 'data/test/result.txt'
    filename = score_test
    with open(filename, 'r') as f:
        lines = f.readlines()
        stu_rank = 0
        stu_faculty = 0
        for line in lines:
            info = line.strip().split(',')
            if stu_id == int(info[0]):
                stu_rank = int(info[2])
                stu_faculty = int(info[1])
                #print "id is: %s \nfaculty is: %s \nrank is: %s" \
                #    %(stu_id, stu_faculty, stu_rank)
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
            max_rank = 0.1
            return_list = [stu_rank, max_rank]
                
    return return_list
'''
a, b= get_score_data(22)    
print a, b
'''

#a, b = get_score_data(0)    
#print a, b
def write_rank_test():
    card_dir = '../data/card_test/'
    list_id = []
    for stu_id in os.listdir(card_dir):
        stuid = int(stu_id.split('.')[0])
        list_id.append(stuid)
    list_id = sorted(list_id)
    
    
    with open('../data/test/rank.txt', 'w') as f:
        for stu_id in list_id:
            stu_rank, max_rank = get_score_data(stu_id)
            rank = float(stu_rank) / float(max_rank)
            row = [stu_id, rank]
            #print row
            writer=csv.writer(f)
            writer.writerow(row)