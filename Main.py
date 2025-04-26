import os
import re

import numpy as np
import pandas as pd
from flask import render_template
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.feature_selection import RFE

global filename
#feature_cols = ['userid','art_galleries','dance_clubs','juice_bars','restaurants','museums','resorts','parks_picnic_spots','beaches','theaters','religious_institutions']
feature_cols = ['userid','dance_clubs','restaurants','museums','resorts','theaters','religious_institutions']
global clf
global rfe
global X_train
global y_train
global fit

def upload():
    global filename
    filename = "dataset.txt"
    with open(filename, "r") as file:
      for line in file:
         line = line.strip('\n')
         print(line)

def featureSelection():
    global clf
    global rfe
    global fit
    global X_train
    global y_train
    dataset = pd.read_csv(filename)
    dataset.head()
    y = dataset['location']
    X = dataset.drop(['location'], axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
    clf = DecisionTreeClassifier()
    rfe = RFE(clf)
    fit = rfe.fit(X_train,y_train)
    print("Total number of features : "+str(len(feature_cols))+"\n")
    print("Selected number of features : "+str(fit.n_features_)+"\n")
    print("Selected number of features : "+str(fit.support_)+"\n")

def decisionTree():
    global clf
    global X_train
    global y_train
    clf.fit(X_train,y_train)
    r = export_text(clf, feature_names=feature_cols)
    print("Selected number of features : "+str(r)+"\n")

def predict():
    global clf
    testname = "file.txt"
    with open(testname, "r") as file:
        for line in file:
            line = line.strip('\n')
    test = pd.read_csv(testname)
    y_pred = clf.predict(test)
    print("\nPredicted Location : "+str(y_pred)+"\n")
    x=y_pred[0]
    print(y_pred[0])
    l=x.split('-')
    print(l)
    '''print(type(x.split('-')))'''
    #return str(x.split('-'))
    return render_template('output.html',names=l)

#def output():


