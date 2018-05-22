# -*- coding: utf-8 -*-

from __future__ import print_function

# The usual suspects ...
import numpy as np
import graphviz

# And the accomplices ...
from IPython.display import Image
from graphviz import Source
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomforestClassifier
from sklearn.metrics import accuracy_score

# Loading the data
iris = load_iris()

X, y, features = iris.data, iris.target, iris.feature_names

# Splitting the data
X_train, X_test, y_train, y_test = train_test_test_split(X, y, test_size=.2, random_state=5, shuffle=True)

# Training
# 1. Decision Tree
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('Decision Tree Accuracy Score: {}'.format(accuracy_score(y_test, y_pred)))

# Visualization
graph = Source(export_graphviz(clf, out_file=None, feature_names=features))
png_bytes = graph.pipe(format='png')
with open('dt.dot', 'wb') as f:
  f.write(png_bytes)
Image(png_bytes)

# 2. K-Nearest Neighbor
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('K-Nearest Neighbor Accuracy Score: {}'.format(accuracy_score(y_test, y_pred)))

# 3. Neural Net
clf = MLPClassifier(max_iter=2000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('Neural Network Accuracy Score: {}'.format(accuracy_score(y_test, y_pred)))

# 4. Random Forest
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
print('Random Forest Accuracy Score: {}'.format(accuracy_score(y_test, y_pred)))
