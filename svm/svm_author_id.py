#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
Cval = 10000
clf = SVC(kernel = "rbf", C = Cval)

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
t0 = time()
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 
clf.fit(features_train, labels_train)
print "training time: ", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t0,3), "s"
print "Chris:",pred.tolist().count(1)
score = accuracy_score(pred, labels_test)
print "With C = ", Cval, " Accuracy: ", score
print "answer at 10:", pred[10]
print "answer at 26:", pred[26]
print "answer at 50", pred[50]



#########################################################
### your code goes here ###

#########################################################


