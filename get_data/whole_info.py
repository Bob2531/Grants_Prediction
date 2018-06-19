# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 01:03:15 2018

@author: bob
"""
import pandas as pd
import matplotlib.pyplot as plt

def get_whole_file():
    card = pd.read_csv('../data/test/draw_card.csv')
    dorm = pd.read_csv('../data/test/draw_dorm.csv', names=[
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
     '22_00enterDiv'])
     
    draw = pd.merge(card, dorm, how='right', on='stuId')

def extract(stuId):
    draw = pd.read_csv('data/test/whole.csv') # remember to remove '../'
    series = draw[draw['stuId'] == stuId]
    value = []
    value.extend(series['library'].values)
    value.extend(series['hospital'].values)
    value.extend(series['shower'].values)
    value.extend(series['academic_office'].values)
    value.extend(series['washer'].values)
    value.extend(series['canteen'].values)
    value.extend(series['market'].values)
    value.extend(series['bus'].values)
    value.extend(series['printing'].values)
    value.extend(series['water'].values)
    value.extend(series['other'].values)
    value.extend(series['06_00enterDiv'].values)
    value.extend(series['06_00exitDiv'].values)
    value.extend(series['09_00exitDiv'].values)
    value.extend(series['09_00enterDiv'].values)
    value.extend(series['12_50exitDiv'].values)
    value.extend(series['12_50enterDiv'].values)
    value.extend(series['11_20exitDiv'].values)
    value.extend(series['11_20enterDiv'].values)
    value.extend(series['16_50exitDiv'].values)
    value.extend(series['16_50enterDiv'].values)
    value.extend(series['19_00exitDiv'].values)
    value.extend(series['19_00enterDiv'].values)
    value.extend(series['22_00exitDiv'].values)
    value.extend(series['22_00enterDiv'].values)
    return value

x_label = ['library',
    'hospital',
    'shower',
    'academic_office',
    'washer',
    'canteen',
    'market',
    'bus',
    'printing',
    'water',
    'other',
    '06_00enterDiv',
    '06_00exitDiv',
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

def draw(stuId, i):
    info = extract(stuId)
    plt.title("Infomation of Single Student")
    plt.xlabel("Items")
    plt.ylabel("Percentage")
    plt.ylim(-0.1,0.8)
    plt.xticks(rotation=90)
    try:
        plt.scatter(x_label, info)
        plt.show()
        save_name = str(stuId) + '.png'
        plt.savefig('../data/'+i+'/' + save_name)
    except ValueError:
        print(str(stuId) + ' has error')
'''
df = pd.read_csv('data/train/X_train.csv')

for i in [0, 1, 2, 3]:# 循环遍历0~ 3 的同学  分别在0, 1, 2, 3文件夹里面生成对应的图
    id_list = df[df['labels'] == i]['stuId'].values.tolist()
    for stu in id_list:
        draw(stu, i)

'''








