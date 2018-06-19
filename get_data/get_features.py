#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:28:05 2018

@author: hadoop
"""
import csv
import card
import os
import change2

global path
path = '/home/bob/Desktop/plot'

def deal_dorm():
    with open('../data/train/DormProcessed.txt', 'r') as f:
        lines = f.readlines()
    t_or_t = '../data/train'
    target = '/draw_dorm.csv'
    target_path = t_or_t + target
    with open(target_path, 'w') as csvfile: 
        for line in lines:
            info=eval(line)
            keys = [
 'stuId',
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
 '22_00enterDiv']
            row = []
            for each_key in keys:
                row.append(info[each_key])
            #labels, values = change2.separate(info)
            writer=csv.writer(csvfile)
            writer.writerow(row)
            #print row
            '''
            stuId=a['stuId']
            timesPerDay=round(a['timesPerDay'], 2)
            totalDays=a['totalDays']
            weekendTimes=a['weekendTimes']
            #print stuid,per,totaldays,weekendTimes
            col_name = [stuId, timesPerDay, totalDays, weekendTimes]
           
            print col_name        
    
            writer=csv.writer(csvfile)
            writer.writerow(col_name)
            '''

def deal_library():
    with open('../data/train/LibraryProcessed.txt', 'r') as f:
        lines = f.readlines()
    t_or_t = '../data/train/'
    target = '/library.csv'
    target_path = path + target    
    with open(target_path, 'w') as csvfile: 
        for line in lines:
            info=eval(line)
            labels, values = change2.separate(info)
            writer=csv.writer(csvfile)
            writer.writerow(values)
            #print values
            '''
            #print info.keys()
            stuId = info['stuId']
            totalDays = info['totalDays']
            totalRecordTimes = info['totalRecordTimes']
            weekendTimes = info['weekendTimes']
            timesPerDay = info['timesPerDay(Div)']
            #col_name = [stuId, totalDays, weekendTimes, totalRecordTimes]
            col_name = [stuId, timesPerDay]
            print col_name        
    
            writer=csv.writer(csvfile)
            writer.writerow(col_name)
            '''

def deal_borrow():
    with open('../data/train/BorrowProcessed.txt', 'r') as f:
            lines = f.readlines()
    t_or_t = '../data/train/'
    target = '/borrow.csv'
    target_path = path + target
    with open(target_path, 'w') as csvfile: 
        for line in lines:
            info=eval(line)
            labels, values = change2.separate(info)
            writer=csv.writer(csvfile)
            writer.writerow(values)
            #print values
            '''
            stuId = info['stuId']
            numOfBorrowed = info['numOfBorrowed']
            ifBorrowed = info['ifBorrowed']
            
            col_name = [stuId, ifBorrowed, numOfBorrowed]
           
            print col_name        
            '''
            
        

def ifKeyerror(col, dic):
    try:
        value = dic[col]
    except KeyError:
        value = 0.
    return round(value, 2)
    

def deal_card():
    col_name = ['stuId', 'library', 'hospital', 'market', 'water', 'canteen', 'washer',
                'other', 'academic_office', 'printing', 'bus', 'shower']
    
    card_dir = '../data/card_train/'
    list_id = []
    for stu_id in os.listdir(card_dir):
        stuid = int(stu_id.split('.')[0])
        list_id.append(stuid)
    list_id = sorted(list_id)
    
    with open('../data/train/draw_card.csv','w') as f:
        for stu_id in list_id:
            consume_dic = card.get_card(stu_id)
            one_row = []
            one_row.append(stu_id)
            for col in col_name[1:]:
                value = ifKeyerror(col, consume_dic)
                one_row.append(value)
            #print one_row
            writer = csv.writer(f)
            writer.writerow(one_row)

def deal_card1():
    col_name = ['stuId', 'library', 'hospital', 'market', 'water', 'canteen', 'washer',
                'other', 'academic_office', 'printing', 'bus', 'shower']
    
    card_dir = '../data/card_train/'
    list_id = []
    for stu_id in os.listdir(card_dir):
        stuid = int(stu_id.split('.')[0])
        list_id.append(stuid)
    list_id = sorted(list_id)
    
    with open('../data/train/card_mean.csv','w') as f:
        for stu_id in list_id:
            consume = card.get_card_mean(stu_id)
            one_row = []
            one_row.append(stu_id)
            for single in consume:
                one_row.append(single)
            #print one_row
            writer = csv.writer(f)
            writer.writerow(one_row)

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
    
