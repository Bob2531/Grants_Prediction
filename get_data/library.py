# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:13:31 2018

@author: bob
"""
import readFromFile
import change2

'''
parameter: stu_id
searching how many times does this student go to the library in 2013.9.1~2014.8.31
return a list : [ months, times ]
'''
def librarytime(stu_id):
    lib_train = 'data/train/library_train.txt'
    lib_test = 'data/test/library_final_test.txt'
    filepath = lib_test
    lines = readFromFile.readLines(filepath)
    librarytimes = {}
    for line in lines:
        sid = int(line.split(',')[0])
        if stu_id == sid:
            year = int(line.split(',')[-1].split()[0].split('/')[0].strip('\"'))
            month = int(line.split(',')[-1].split()[0].split('/')[1].strip('\"'))
            if year == 2013:
                if month in librarytimes:
                    librarytimes[month] += 1
                else :
                    librarytimes[month] = 1
            if year == 2014:
                if month in librarytimes:
                    librarytimes[month] += 1
                else :
                    librarytimes[month] = 1
                    
    months, times = change2.separate(librarytimes)
    return [months, times]
#print librarytimes 