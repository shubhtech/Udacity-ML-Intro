#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 



#########################################################
### your code goes here ###
#start = time.time()
t0 = time()
#clf = SVC(kernel='linear')
clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train, labels_train)
print ('training time:' + str(round(time()-t0,3)) +'s')

t0 = time()
pred = clf.predict(features_test)
print ('predicting time:' + str(round(time()-t0,3)) + 's')

print ('accuracy:'+str(accuracy_score(pred,labels_test)))

#print (pred[10])
#print (pred[26])
#print (pred[50])

#len(pred)
n = []
[n.append(e) for e in pred if e == 1]
print(len(n))

#########################################################
