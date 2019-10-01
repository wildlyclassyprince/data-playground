'''
modeling.py

Classification Task Functions
'''

# Header
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# The usual suspects ...
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Metrics
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

# Utilities
from sklearn.utils.multiclass import unique_labels
from collections import Counter

# Pipeline Functions
# Modeling:
# 1. Train
def train_model(X_train, y_train, model):
    '''Returns trained model.'''
    return model.fit(X_train, y_train)

# 2. Predict
def predict(X_test, model):
    '''Returns predictions from trained model.'''
    return model.predict(X_test)

# Evaluation
# 1. Metrics
def prediction_metrics(actual, predictions, names, model_name):
    '''Calculates the prediction metrics for a classification task.
    
    actual : series
        True values not used in the training process.
    predictions : series
        Values obtained from prediction evaluation.
    names: list
        List of model names used in the pipeline.
    model_name: string
        Name of the model to evaluate metrics.
        
    Returns: dataframe
    Precision
        Indicator of the number of items correctly identified as positive
        out of the total items identified as positive.
    Recall
        indicator of the number of items correcty identified as positive
        out of total actual positives.
    F1
        Performance score that combines both precision and recall. A
        harmonic mean of the two variables.
    '''
    # Metrics
    try:
        precision = precision_score(predictions, actual)
        recall = recall_score(predictions, actual)
        f1 = f1_score(predictions, actual)
    except:
        pass
    # Results
    results = pd.DataFrame(columns=['Precision', 'Recall', 'F1'],
                           index=names)
    results.loc[model_name, :] = [precision, recall, f1]
    
    return results

# 2. Confusion Matrix
def plot_confusion_matrix(actual, predictions, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    '''Plots the confusion matrix. Normalization can be applied by
    setting `normalize=True`.
    actual : series
        True values not used in the training process.
    predictions : series
        Values obtained from prediction evaluation.
    classes: array
        Class definitions
    '''

    if not title:
        if normalize:
            title = 'Normalized Confusion Matrix'
        else:
            title = 'Non-normalized Confusion matrix'
    
    # Confusion matrix
    cm = confusion_matrix(actual, predictions)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(actual, predictions)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    # Plot
    plt.figure(figsize=(12, 8))
    ax = plt.subplot()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    # We wish to show all ticks ...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           ylabel='True',
           xlabel='Predicted')
    ax.set_title(title, fontsize=16)
    
    # Rotate the tick labels and set their alignment
    plt.setp(ax.get_xticklabels(), 
             rotation=45,
             ha='right',
             rotation_mode='anchor')
    
    # Loop over data dimensions and create text annotations
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha='center', va='center',
                    color='white' if cm[i, j] > thresh else 'black')
    plt.tight_layout()
    plt.show()
    
# 3. Plot Results
def plot_results(results):
    '''Plots barplots of model results.'''
    plt.figure(figsize=(30, 8), edgecolor='black')
    for i, metric in enumerate(results.columns):
        ax = plt.subplot(1, 3, i+1)
        results.sort_values(metric, ascending=True).plot.barh(y=metric,
                                                              color='b',
                                                              ax=ax)
        plt.title(metric, fontsize=16)
        plt.xlabel(' ')
        plt.grid()
        plt.tight_layout()