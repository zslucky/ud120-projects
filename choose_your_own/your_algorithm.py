#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

from time import time
from sklearn.neighbors import  KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=5)

t0 = time()
clf.fit(features_train, labels_train)
print "training time: ", (time() - t0), 's'

t1 = time()
accuracy = clf.score(features_test, labels_test)
print "prediction time: ", (time() - t1), 's'

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass


# KNN
#########################################################
### Result:

#### n_neighbors=3
###### - accuracy: 0.978953356086
###### - training time: 74.8643209934 s
###### - prediction time: 0.0397131443024 s

#### n_neighbors=10
###### - accuracy: 0.967007963595
###### - training time: 5.15142321587 s
###### - prediction time: 0.00214195251465 s

#########################################################