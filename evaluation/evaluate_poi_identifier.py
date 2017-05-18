#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
import numpy as np
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()

clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

'''
  get precision and recall
'''
from sklearn.metrics import precision_score, recall_score

precision_accuracy = precision_score(labels_test, pred)
recall_accuracy = recall_score(labels_test, pred)

print "precision_accuracy = ", precision_accuracy
print "recall_accuracy = ", recall_accuracy

'''
  compare pred and labels
'''
# print zip(pred, labels_test)

'''
  pred are all 0 not POI
  result: 0.862068965517
'''
# from sklearn.metrics import accuracy_score

# accuracy = accuracy_score(labels_test, np.asarray([0 for i in range(29)]))
# print accuracy

'''
  POI numbers
'''
# print np.sum(pred)

'''
  simple decision tree accuracy
'''
# accuracy = clf.score(features_test, labels_test)
# print(accuracy)