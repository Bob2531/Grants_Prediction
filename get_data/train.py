#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:34:15 2018

@author: hadoop
"""

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn import metrics

from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

#clf = GaussianNB()
clf = RandomForestClassifier()
train_sample = pd.read_csv('../data/train/card_meann.csv', dtype=np.float)#load sample from train.csv
test_sample = pd.read_csv('../data/test/X_test.csv', dtype=np.float)#load sample from test.csv
test_sample = test_sample.fillna(0.)

def showFeatureImportances(featureImportance, columns):
    featureImportances = featureImportance / featureImportance.max()
    idxSorted = np.argsort(featureImportances)
    barPos = np.arange(idxSorted.shape[0]) + .5
    plt.barh(barPos, featureImportances[idxSorted], align='center')
    plt.yticks(barPos, columns[idxSorted])
    plt.xlabel('Variable Importance')
    plt.show()

def model_test(sample):
    '''
    dataset = sample[[u'library', u'hospital', u'market', u'water', u'canteen',
           u'washer', u'other', u'academic_office', u'printing', u'bus', u'shower',
           u'ifBorrowed', u'numOfBorrowed', u'DormtimesPerDay', u'DormtotalDays',
           u'DormweekendTimes', u'librarytotalDays', u'libraryweekendTimes',
           u'librarytotalcol_nameTimes', u'ranks', u'labels']].values
    '''
    dataset = sample[[u'library', u'hospital', u'market', u'water', u'canteen', u'washer',
                u'other', u'academic_office', u'printing', u'bus', u'shower', u'labels']].values
    #X_train, X_test, y_train, y_test = train_test_split(dataset, y, random_state=14)

    i = np.random.permutation(len(dataset))
        
    train_size = int(len(i) * 0.8)
    
    X_train = dataset[i[:train_size]]
    X_test = dataset[i[train_size:]]
    y_train = dataset[i[:train_size]]
    y_test = dataset[i[train_size:]]
    
    X_train = X_train[:,:-2]
    X_test = X_test[:, :-2]
    y_train = y_train[:, -1]
    y_test = y_test[:, -1]
    
    stuId = sample['stuId'].values[i[train_size:]]    
    '''
    x = []
    y= []
    #for rando in range(1, 30):
    rando = 4
    n_estimators=rando
    n_jobs=12
    max_depth=12
    min_sample_split=rando
    min_samples_leaf=5
    max_leaf_nodes=100
    clf = RandomForestClassifier(n_estimators=10000,     
                                 n_jobs=n_jobs,
                                 criterion='gini',
                                 max_depth=max_depth, 
                                 min_samples_leaf=min_samples_leaf,
                                 max_leaf_nodes=max_leaf_nodes
                                 )

#test model
#X_train, X_test, y_train, y_test, stuId = model_test(sample)
    '''
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)  
    y_predict_label = clf.predict_proba(X_test)
    #print(dtree.tree_.feature)    
    
    accuracy = np.mean(y_test == y_predict) 
    print "accuracy is %f" %(accuracy)
    featureImportance = clf.feature_importances_
    #get columns
    cols = sample.columns
    #showFeatureImportances(featureImportance, cols)
    x.append(rando)
    y.append(accuracy)
    '''
    plt.title("Accuracy")
    plt.xlabel("Times of max_leaf_nodes")
    plt.ylabel("Accuracy")
    plt.plot(x, y)
    plt.show()
    '''   
    return y_test, y_predict
    
    #return X_train, X_test, y_train, y_test, stuId
    
def model(train_sample, test_sample):
    dataset_train = train_sample[[u'library', u'hospital', u'market', u'water', u'canteen',
           u'washer', u'other', u'academic_office', u'printing', u'bus', u'shower',
           u'ifBorrowed', u'numOfBorrowed', u'DormtimesPerDay', u'DormtotalDays',
           u'DormweekendTimes', u'librarytotalDays', u'libraryweekendTimes',
           u'librarytotalcol_nameTimes', u'ranks']].values
    i = np.random.permutation(len(dataset_train))
    
    dataset_train = dataset_train[i]
    
    X_train = dataset_train
    y_train = train_sample['labels'].values[i]
    
    dataset_test = test_sample[[u'library', u'hospital', u'market', u'water', u'canteen',
           u'washer', u'other', u'academic_office', u'printing', u'bus', u'shower',
           u'ifBorrowed', u'numOfBorrowed', u'DormtimesPerDay', u'DormtotalDays',
           u'DormweekendTimes', u'librarytotalDays', u'libraryweekendTimes',
           u'librarytotalcol_nameTimes', u'ranks']].values
    i = np.random.permutation(len(dataset_test))
    X_test = dataset_test[i]    
    stu_Id = test_sample['stuId'].values[i]
    return X_train, y_train, X_test, stu_Id
    
def write_to_result(X_test, stuId):
    proba = []
    index = 0
    probability = clf.predict_proba(X_test)
    for stuid, pro in zip(stuId, probability):
        get_in = np.mean(pro[1:])
        #print get_in, get_out
        row = [int(stuid), get_in]
        proba.append(row)
        index += 1
        
    array = np.array(proba)
    sort_array = array[np.lexsort(array[:,::-1].T)]  
    
    with open('../data/test/probability.csv', 'w') as f:
        for stuid, pro in sort_array:
            final =  [int(stuid), pro]
            writer=csv.writer(f)
            writer.writerow(final)
            
def write_to_commit(X_test, stuId):
    proba = []
    index = 0
    probability = clf.predict(X_test)
    for stuid, pro in zip(stuId, probability):
        if pro == 0:
            category = 0
        if pro == 1:
            category = 1000
        if pro == 2:
            category = 1500
        if pro == 3:
            category = 2000
        row = [int(stuid), category]
        proba.append(row)
        index += 1    

    array = np.array(proba)
    sort_array = array[np.lexsort(array[:,::-1].T)]    
    
    with open('../commit.csv', 'w') as f:
        for stuid, pro in sort_array:
            final =  [stuid, pro]
            writer=csv.writer(f)
            writer.writerow(final)
'''
#test model
X_train, X_test, y_train, y_test, stuId = model_test(sample)

accuracy = np.mean(y_test == y_predict) 
print "accuracy is %f" %(accuracy)
'''
'''
X_train, y_train, X_test, stu_Id = model(train_sample, test_sample)

clf.fit(X_train, y_train)
y_predict = clf.predict(X_test)

write_to_commit(X_test, stu_Id)
write_to_result(X_test, stu_Id)
'''

def return_num(target_list):
    for each in range(len(target_list)):
        if target_list[each] == 0:
            target_list[each] = 1
    return target_list        

def ROC(y_test, y_predict):
    y_prob = return_y_predict(y_predict)
    fpr, tpr, thresholds = metrics.roc_curve(y_test, y_prob, pos_label=2)

    print fpr, tpr, thresholds    
    
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',lw=lw)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()

def return_y_predict(y_predict):
    y_prob = []
    for example in y_predict:
        get_prob = example[1:].mean()
        y_prob.append(get_prob)
    return y_prob

y_test, y_predict = model_test(train_sample)
f1_score = metrics.f1_score(y_test, y_predict, average=None)
print f1_score
#ROC(y_test, y_predict)
