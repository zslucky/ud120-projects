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


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

clf = svm.SVC(kernel='rbf', C=10000.)
t0 = time()
clf.fit(features_train, labels_train)
print 'training time: ', (time() - t0), 's'

# t1 = time()
# accuracy = clf.score(features_test, labels_test)
# print 'prediction time: ', (time() - t1), 's'

t1 = time()
pred = clf.predict(features_test)
print 'prediction time: ', (time() - t1), 's'

print sum(pred)

# print accuracy

#########################################################

#########################################################
### Result:

#### kenel=linear
###### - accuracy: 0.984072810011
###### - training time: 214.120304823s
###### - prediction time: 24.7667920589s


#### kenel:linear, train_dataset/100
###### - accuracy: 0.884527872582
###### - training time: 0.124592065811s
###### - prediction time: 1.20096516609s

### kernel:rbf, C=1.0, train_dataset/100
###### - accuracy: 0.616040955631
###### - training time: 0.135191917419s
###### - prediction time: 1.38017487526s

### kernel:rbf, C=10.0, train_dataset/100
###### - accuracy: 0.616040955631
###### - training time: 0.12451505661s
###### - prediction time: 1.30438303947s

### kernel:rbf, C=100.0, train_dataset/100
###### - accuracy: 0.616040955631
###### - training time: 0.133071184158s
###### - prediction time: 1.38506817818s

### kernel:rbf, C=1000.0, train_dataset/100
###### - accuracy: 0.821387940842
###### - training time: 0.121322870255s
###### - prediction time: 1.30741095543s

### kernel:rbf, C=10000.0, train_dataset/100
###### - accuracy: 0.892491467577
###### - training time: 0.125902175903s
###### - prediction time: 1.09894704819s

### kernel:rbf, C=10000.0
###### - accuracy: 0.990898748578
###### - training time: 136.757467031s
###### - prediction time: 13.2800681591s

#########################################################