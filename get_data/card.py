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
    card_dir = 'data/card/' #card_file's dir
    for file_name in os.listdir(card_dir):
        target_name = int(file_name.split('.')[0]) #['18800', 'csv']
        if stu_id == target_name:
            print "target_path is : ", card_dir + file_name
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
        filepath = read_id(stu_id)
    except IOError:
        print "No such a file or dir"
        return
    lines = readFromFile.readLines(filepath)
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
        print "No such a file or dir"
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
        labels, values = separate(pay_sum)
        #values = change2.change(values)#change format items in values
    return [labels, values]

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
    values = change2.change(values)
    return labels, values

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
        label, value = separate(month[1])
        month[1] = round(sum(value), 2)
    return pre_list

'''
pre_list = month_sum(22)
print pre_list
'''    
    
    
    
    
    
    
    
    
    
    
    
    
    
    