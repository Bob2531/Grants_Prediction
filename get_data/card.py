#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 23:46:52 2018

@author: hadoop
"""

#import sys
import readFromFile
import os
import change2
import numpy as np
global file_path

def create_each_list():
    pay_sum = []
    for month_numb in range(1,13):
        mon_dic = {}
        mon = [month_numb, mon_dic]
        pay_sum.append(mon)
    return pay_sum

def type_mapping(chinese):
    if chinese == "图书馆":
        return "library"
    elif chinese == "校医院":
        return "hospital"
    elif chinese == "超市":
        return "market"
    elif chinese == "开水":
        return "water"
    elif chinese == "食堂":
        return "canteen"
    elif chinese == "洗衣房":
        return "washer"
    elif chinese == "其他":
        return "other"
    elif chinese == "教务处":
        return "academic_office"
    elif chinese == "文印中心":
        return "printing"
    elif chinese == "校车":
        return "bus"
    else:
        return "shower"

'''
parameter: stu_id  is the student's id 
return a consume filepath by searching with student id
'''
def read_id(stu_id):
    card_dir_train = 'data/card_train/' #card_file's dir
    card_dir_test = 'data/card_test/' #card_file's dir
    card_dir = card_dir_test
    for file_name in os.listdir(card_dir):
        target_name = int(file_name.split('.')[0]) #['18800', 'csv']
        if stu_id == target_name:
            #print "target_path is : ", card_dir + file_name
            file_path = card_dir + file_name
    #return each_month(file_path)
    return file_path
            
'''
get consume data with 2013.9.1 ~ 2014.8.31
return a list which contains 12 lists
each structure just like this: [ [month 1, dict]
                                 [month 2, dict]
                                 .
                                 .
                                 .
                                 [month 12, dict] ]
ecah dict is labels:value
for instance :      bus: 120  
'''
def each_month(stu_id):
    try:
        each_filepath = read_id(stu_id)
    except IOError:
        #print "No such a file or dir"
        return
    lines = readFromFile.readLines(each_filepath)
    pay_types = ['POS消费', '卡充值']
    #create result list 
    pay_sum = create_each_list()
    
    for line in lines[0:]:
        info = line.split(',')
        if info[1] == pay_types[0]:#POS消费
            year = int(info[4].split()[0].split('/')[0])
            month = int(info[4].split()[0].split('/')[1])
            consume_type = info[3]
            if year == 2013:
                for amonth in range(9, 13):
                    consume_name = type_mapping(consume_type)
                    #print consume_name
                    if consume_name in pay_sum[month-1][1]:
                        pay_sum[month-1][1][consume_name] += float(info[5])
                    else:
                        pay_sum[month-1][1][consume_name] = float(info[5])
            if year == 2014:
                for amonth in range(1, 9):
                    consume_name = type_mapping(consume_type)
                    #print consume_name
                    if consume_name in pay_sum[month-1][1]:
                        pay_sum[month-1][1][consume_name] += float(info[5])
                    else:
                        pay_sum[month-1][1][consume_name] = float(info[5])
    return pay_sum

'''
get consume data with 2013.9.1 ~ 2014.8.31
return a list contains labels(type:list) and values(type:list)
just like this: [labels, values] 
'''
def all_month(stu_id):
    try:
        filepath = read_id(stu_id)
    except IOError:
        #print "No such a file or dir"
        return
    lines = readFromFile.readLines(filepath)
    pay_types = ['POS消费', '卡充值']
    #create result list 
    pay_sum = {}
    
    for line in lines[0:]:
        info = line.split(',')
        if info[1] == pay_types[0]:#POS消费
            year = int(info[4].split()[0].split('/')[0])
            consume_type = info[3]
            if year == 2013:
                for amonth in range(9, 13):
                    consume_name = type_mapping(consume_type)
                    if consume_name in pay_sum:
                        pay_sum[consume_name] += float(info[5])
                    else:
                        pay_sum[consume_name] = float(info[5])
            if year == 2014:
                for amonth in range(1, 9):
                    consume_name = type_mapping(consume_type)
                    if consume_name in pay_sum:
                        pay_sum[consume_name] += float(info[5])
                    else:
                        pay_sum[consume_name] = float(info[5])
        labels, values = change2.separate(pay_sum)
        #values = change2.change(values)#change format items in values
    return [labels, values]
    
'''
parameter student's id
func: get the monthly sum of consume
return a list like this:
[   [1, 2604.4]
    [2, 853.44]
    [3, 4762.64]
    [4, 6302.4]
    [5, 4007.04]
    [6, 3900.0]
    [7, 1865.6]
    [8, 612.96]
    [9, 1884.8]
    [10, 1626.24]
    [11, 1989.6]
    [12, 1707.48] ]
'''
def month_sum(stu_id):
    pre_list = each_month(stu_id)
    for month in pre_list:
        label, value = change2.separate(month[1])
        month[1] = round(sum(value), 2)
    return pre_list

'''
pre_list = month_sum(22)
print pre_list
'''    

def get_card(stu_id):
    try:
        filepath = read_id(stu_id)
    except IOError:
        #print "No such a file or dir"
        return
    lines = readFromFile.readLines(filepath)
    pay_types = ['POS消费', '卡充值']
    #create result list 
    pay_sum = {}
    
    for line in lines[0:]:
        info = line.split(',')
        if info[1] == pay_types[0]:#POS消费
            year = int(info[4].split()[0].split('/')[0])
            consume_type = info[3]
            if year == 2013:
                for amonth in range(9, 13):
                    consume_name = type_mapping(consume_type)
                    if consume_name in pay_sum:
                        pay_sum[consume_name] += float(info[5])
                    else:
                        pay_sum[consume_name] = float(info[5])
            if year == 2014:
                for amonth in range(1, 9):
                    consume_name = type_mapping(consume_type)
                    if consume_name in pay_sum:
                        pay_sum[consume_name] += float(info[5])
                    else:
                        pay_sum[consume_name] = float(info[5])
            if year == 2014:
                for amonth in range(9, 13):
                    consume_name = type_mapping(consume_type)
                    if consume_name in pay_sum:
                        pay_sum[consume_name] += float(info[5])
                    else:
                        pay_sum[consume_name] = float(info[5])
            if year == 2015:
                for amonth in range(1, 9):
                    consume_name = type_mapping(consume_type)
                    if consume_name in pay_sum:
                        pay_sum[consume_name] += float(info[5])
                    else:
                        pay_sum[consume_name] = float(info[5])
    return pay_sum

def get_card_mean(stu_id):
    try:
        filepath = read_id(stu_id)
    except IOError:
        #print "No such a file or dir"
        return
    lines = readFromFile.readLines(filepath)
    
    consume_types = ['library', 'hospital', 'market', 'water', 'canteen', 'washer',
                    'other', 'academic_office', 'printing', 'bus', 'shower']
    return_array = []    
    for types in consume_types:
        record = []
        times = 0
        consume_sum = []
        consume_mean = 0.
        for line in lines[:]:
            info = line.split(',')
            consume_type = info[3]
            consume_name = type_mapping(consume_type)
            pays = float(info[-2])
            if pays == 0.0:
                continue
            if info[1] == 'POS消费':
                if consume_name == types:
                    consume_sum.append(pays)
                    times += 1
                    #print consume_name, consume_sum, times
                    consume_mean = np.array(consume_sum).sum() / len(consume_sum)
                    record.append(consume_mean)
    
        return_array.append(consume_mean)
    return return_array

def changeX(dataset):
    XX = dataset
    for index, row in XX.iterrows():
        col_name = [u'library', u'hospital', u'market', u'water', u'canteen',
           u'washer', u'other', u'academic_office', u'printing', u'bus', u'shower']
        all_pay = row[col_name].sum()
        for fea_name in col_name:
            row[fea_name] = row[fea_name] / all_pay
        XX.ix[index] = row
    return XX             
            
       