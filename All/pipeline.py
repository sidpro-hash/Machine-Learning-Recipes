__author__ = "Siddharth Gabu"
__license__ = "MIT"
__version__ = "1.0"
__credits__ = "Josh Gordon - Google Developers"
__maintainer__ = "Siddharth Gabu"
__status__ = "Practice"


import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5) # 0.5 for half train and half test

'''we can just change these two lines '''
#from sklearn import tree
#clf = tree.DecisionTreeClassifier()
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()

clf.fit(X_train,y_train)
prediction = clf.predict(X_test)
#print(prediction)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,prediction))