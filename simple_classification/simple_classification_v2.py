# -*- coding: utf-8 -*-

from __future__ import print_function

# The usual suspects ...
# And the accomplices ...
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Loading the data
iris = load_iris()

X, y, features = iris.data, iris.target, iris.feature_names

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=5, shuffle=True)

# Training and testing
for i in zip(['Decision Tree', 'K-Nearest Neighbor', 
              'Neural Net', 'Random Forest'],
             [DecisionTreeClassifier(), KNeighborsClassifier(),
              MLPClassifier(max_iter=2000), RandomForestClassifier()]):
    name, clf = i
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(name, 'Accuracy Score: \t{}'.format(accuracy_score(y_test, y_pred)))
