#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print len(features_train[0])

#########################################################
### your code goes here ###
from sklearn import tree

clf = tree.DecisionTreeClassifier(min_samples_split=40)
t0 = time()
clf.fit(features_train, labels_train)
print 'training time: ', (time() - t0), 's'

t1 = time()
accuracy = clf.score(features_test, labels_test)
print 'prediction time: ', (time() - t1), 's'

print accuracy

#########################################################


#########################################################
### Result:

#### min_samples_split=40, percentTile=10
###### - accuracy: 0.978953356086
###### - training time: 74.8643209934 s
###### - prediction time: 0.0397131443024 s

#### min_samples_split=40, percentTile=1
###### - accuracy: 0.967007963595
###### - training time: 5.15142321587 s
###### - prediction time: 0.00214195251465 s

#########################################################