import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

iris = load_iris()

# Training and testing datasets
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

# Decision Tree
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Acccuracy
print("Decision Tree Accuracy Score: {}".format(metrics.accuracy_score(y_test, y_pred)))

# K-Nearest Neighbors
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Acccuracy
print("K-Nearest Neighbors Accuracy Score: {}".format(metrics.accuracy_score(y_test, y_pred)))

# Neural Network
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Acccuracy
print("Neural Net Accuracy Score: {}".format(metrics.accuracy_score(y_test, y_pred)))
