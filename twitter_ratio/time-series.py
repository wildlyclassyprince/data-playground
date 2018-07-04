# -*- coding: utf-8 -*-

# The usual suspects ...
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


# Converting to datetime
def convert_to_datetime(data, column):
    '''Converts a string array to pandas datetime format.'''
    data[column] = pd.to_datetime(data[column], 
                                  yearfirst=True, 
                                  exact=False)

# Creating a time series object
def create_series(data, time_column, category_column):
    '''Create a time series object.'''
    return data.set_index(time_column)[category_column]

# Plotting a time series object
def plot_series(data, title='', ylabel='', color='blue'):
    '''Plotting a time series object.'''
    # Size of the plot
    plt.figure(figsize=(22, 10))
    # Removing plot-frame lines
    ax = plt.subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # Axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    # Limiting the plot-range
    ax.set_xlim(data.index.min(), data.index.max())
    ax.set_ylim(data.values.min(), data.values.max())
    # Trace lines
    for i in range(int(data.values.min()+data.values.max()/2), int(data.values.max()+1), int(data.values.max()/10)):
        plt.plot(range(data.index.year.min(), data.index.year.max()), 
                 [i]*len(range(data.index.year.min(), data.index.year.max())),
                 '--', lw=.5, color='grey', alpha=.3)
    # Removing tick marks
    ax.tick_params(axis='both', which='both', 
                    bottom=False, top=False,
                    labelbottom=True, labelleft=True,
                    left=False, right=False)
    # Plot labels
    ax.set_ylabel(ylabel, fontsize=16)
    # Plotting
    ax.plot(data, color=color)