# -*- coding: utf-8 -*-

# The usual suspects ...
import contextlib
import statsmodels
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# And their accomplices ...
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA

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
def plot_series(data,  title, ylabel, data2=None, data3=None, color='blue', color2='red', color3='green'):
    '''Plotting a time series object.'''
    # Input type, missing values & Infinity
    if isinstance(data, pd.Series):
        data.replace([np.inf, np.NaN], 0, inplace=True)
    else:
        raise AttributeError
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
    ax.tick_params(axis='both', size=14)
    # Limiting the plot-range
    ax.set_xlim(data.index.min(), data.index.max())
    ax.set_ylim(data.values.min(), data.values.max())
    # Trace lines
    for i in range(int(data.values.min()+data.values.max()/2), int(data.values.max()+1)):
        plt.plot(range(data.index.year.min(), data.index.year.max()),
                 [i]*len(range(data.index.year.min(), data.index.year.max())),
                 '--', lw=.5, color='grey', alpha=.3)
    # Removing tick marks
    ax.tick_params(axis='both', which='both',
                   bottom=False, top=False,
                   labelbottom=True, labelleft=True,
                   left=False, right=False)
    # Plot labels
    ax.set_title(title, fontsize=24)
    ax.set_ylabel(ylabel, fontsize=18)
    # Plotting
    # To create error bars, use fill_between() with a nice fill color -> #3FD7D
    # ax.fill_between() 
    ax.plot(data, color=color)
    if isinstance(data2, pd.Series):
        data2.replace([np.inf, np.NaN], 0, inplace=True)
        ax.plot(data2, color=color2)
    elif isinstance(data3, pd.Series):
        data3.replace([np.inf, np.NaN], 0, inplace=True)
        ax.plot(data3, color=color3)
    else:
        pass

# Plotting predictions
def plot_predictions(data, data2, title, ylabel, data3=None, color='blue', color2='green', color3='purple'):
    '''Plotting a time series object.'''
    # Input type, missing values & Infinity
    if isinstance(data, pd.Series):
        data.replace([np.inf, np.NaN], 0, inplace=True)
    elif isinstance(data2, pd.Series):
        data2.replace([np.inf, np.NaN], 0, inplace=True)
    elif isinstance(data3, pd.Series):
        data3.replace([np.inf, np.NaN], 0, inplace=True)
    else:
        raise AttributeError
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
    ax.tick_params(axis='both', size=14)
    # Limiting the plot-range
    #ax.set_xlim(data.index.min(), data.index.max())
    #ax.set_ylim(data.values.min(), data.values.max())
    # Trace lines
    #for i in range(int(data.values.min()+data.values.max()/2), int(data.values.max()+1)):
    #    plt.plot(range(data.index.year.min(), data.index.year.max()),
    #             [i]*len(range(data.index.year.min(), data.index.year.max())),
    #             '--', lw=.5, color='grey', alpha=.3)
    # Removing tick marks
    ax.tick_params(axis='both', which='both',
                   bottom=False, top=False,
                   labelbottom=True, labelleft=True,
                   left=False, right=False)
    # Plot labels
    ax.set_title(title, fontsize=24)
    ax.set_ylabel(ylabel, fontsize=18)
    # Plotting
    ax.plot(data, color=color, label='Actual')
    ax.plot(data2, color=color2, label='Predicted')
    if isinstance(data3, pd.Series):
        data3.replace([np.inf, np.NaN], 0, inplace=True)
        ax.plot(data3, color=color3)
    else:
        pass
    # Legend
    ax.legend(loc='best', fontsize='x-large')

# Testing for stationarity
def test_stationarity(data):
    '''Testing for stationarity of a time series.'''
    # Rolling statistics
    rol_mean = data.rolling(window=12, center=False).mean().dropna()
    rol_std = data.rolling(window=12, center=False).std().dropna()

    # Plotting
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
    #ax.set_xlim(data.index.min(), data.index.max())
    #ax.set_ylim(data.values.min(), data.values.max())
    # Trace lines
    #for i in range(int(data.values.min()+data.values.max()/2), int(data.values.max()+1)):
    #    plt.plot(range(data.index.year.min(), data.index.year.max()),
    #             [i]*len(range(data.index.year.min(), data.index.year.max())),
    #             '--', lw=.5, color='grey', alpha=.3)
    # Removing tick marks
    ax.tick_params(axis='both', which='both',
                   bottom=False, top=False,
                   labelbottom=True, labelleft=True,
                   left=False, right=False)
    # Plot labels
    #ax.set_ylabel('Frequency', fontsize=16)
    # Plotting
    ax.plot(data, color='blue', label='Original')
    ax.plot(rol_mean, color='green', label='Rolling Mean')
    ax.plot(rol_std, color='red', label='Standard Deviation')
    ax.legend(loc='best', fontsize='x-large')
    ax.set_title('Rolling Statistics', fontsize=24)
    plt.show(block=True)
    
    # Perform Dickey-Fuller Test:
    print('Results of Dickey-Fuller Test:')
    try:
        df_test = adfuller(data, autolag='AIC')
        df_output = pd.Series(df_test[0:4], index=['Test Statistic',
                                                   'p-value',
                                                   'Number of Lags Used',
                                                   'Number of Observations Used'])
        for key, value in df_test[4].items():
            df_output['Critical Value ({})'.format(key)] = value
        print(df_output)
    except ValueError as v:
        print(v)
    except NameError as n:
        print(n)

# Sliding mean
def sliding_mean(data, window=5):
    '''Smoothing function for ease of plot readability.'''
    data = np.array(data)
    new_list = list()
    for i in range(len(data)):
        indices = range(max(i - window + 1, 0),
                        min(i + window + 1, len(data)))
        avg = 0
        for j in indices:
            avg += data[j]
        avg /= float(len(indices))
        new_list.append(avg)
    return np.array(new_list)
