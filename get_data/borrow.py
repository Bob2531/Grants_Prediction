# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 08:14:43 2018

@author: bob
"""
import change2

'''
get book_name and numbers with dict
and return label(book's name) , value(book's number)
'''
def bookname(stu_id):
    borrow_train = 'data/train/borrow_train_invert.txt'
    borrow_test = 'data/test/borrow_final_test_invert.txt'
    filename = borrow_test
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    book_name = {}
    for line in lines:
        sid = line.strip().split('$')[0]
        if stu_id == int(sid):
            info = line.strip().split('$')[1:]
            for each in info:    
                name = each.split(',')[1].split()[0].strip('"')
                if name in book_name:
                    book_name[name] += 1
                else:
                    book_name[name] = 1
                #print name
    label, value = change2.separate(book_name)
    return [label, value]
