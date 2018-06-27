# -*- coding: utf-8 -*- 

# The usual suspects ...
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import statsmodels 

# And their accomplices ...
from statsmodels.tsa.stattools import adfuller, acf, pacf 
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA

# Creating a time series object
def create_series(data, index_column, series_column):
    '''Creates a time series object.'''
    s = data[[index_column, series_column]]
    series = s.set_index(index_column)[series_column]

# Time series plotting function
def plot_series(series, ylabel, title=None, color='blue'):
    '''Plots a time series object.'''
    plt.figure(figsize=(22, 10))
    plt.plot(series, color=color)
    plt.title(title, fontsize=24)
    plt.xticks(fontsize=12)
    plt.ylabel(ylabel, fontsize=16)
    plt.yticks(fontsize=12)

# Testing for stationarity
def test_stationarity(series):
    '''Tests for stationarity of the time series.'''
    # Determine rolling statistics
    rol_mean = series.rolling(window=12, center=False).mean().dropna()
    rol_std = series.rolling(window=12, center=False).std().dropna()

    # Plot rolling statistics
    plt.figure(figsize=(22, 10))
    orig = plt.plot(series, color='blue', label='Original Time Series')
    mean = plt.plot(rol_mean, color='red', label='Rolling Mean')
    std = plt.plot(rol_std, color='black', label='Rolling Standard Deviation')
    plt.legend(loc='best', fontsize='x-large')
    plt.title('Rolling Statistics', fontsize=24)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show(block=False)

    # Perform Dickey-Fuller Test:
    print('Results of Dickey-Fuller Test:')
    try:
        df_test = adfuller(series, autolag='AIC')
        df_output = pd.Series(df_test[0:4], index=[ 'Test Statistic', 
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