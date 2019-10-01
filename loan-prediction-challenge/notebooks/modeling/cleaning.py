# Header
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# The usual suspects
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

from scipy import stats
from sklearn import preprocessing

# Unique values
def unique_values(dataframe, data_type='object'):
    for i in dataframe.select_dtypes(include=data_type).columns:
        print('Column: {}, Unique: {}'.format(
            i, len(dataframe.select_dtypes(include=data_type)[i].unique())))

# Convert to datetime
def convert_to_datetime(dataframe):
    '''Converts to datetime format.'''
    for column, value in zip(dataframe.columns,
                             dataframe.columns.str.contains('date')):
        if value == True:
            dataframe[column] = pd.to_datetime(dataframe[column],
                                               yearfirst=True,
                                               exact=False)
            
# Convert to category data type
def convert_to_category_type(dataframe):
    '''Converts object data to category data type.'''
    for column in dataframe.select_dtypes(include='object').columns:
        dataframe[column] = dataframe[column].astype('category')

# Label encoding
def label_encoding(dataframe):
    '''Encoding categorical variables.'''
    label_encoder = preprocessing.LabelEncoder()
    for column in dataframe.select_dtypes(include='category').columns:
        dataframe[column] = label_encoder.fit_transform(dataframe[column])

# Text formatting
def lower_case(dataframe):
    _cols = (i for i in dataframe.select_dtypes(include='object').columns)
    try:
        while True:
            _col = _cols.__next__()
            dataframe[_col] = list(map(lambda i: i.lower(), dataframe[_col]))
    except StopIteration:
        print('Done.\n')
    except KeyError:
        print('Nothing to do.\n')

# Frequency plot
def frequency_plot(dataframe, x, title, hue=None):
    '''Duel axis frequency plot with percentages.'''
    # Plot settings
    plt.rcParams['figure.figsize'] = (16.0, 9.0)
    # Size of dataframe
    ncount = len(dataframe)
    # Default chart
    ax = sns.countplot(data=dataframe, x=x, hue=hue)
    plt.title(title, fontsize=16)
    plt.xlabel(' ')
    # Make twin axes
    ax2=ax.twinx()
    # Switch axes - percentages on the left, frequency on the right
    ax2.yaxis.tick_right()
    ax.yaxis.tick_left()
    # Switch labels as well
    ax2.set_ylabel('Percentage')
    ax.set_ylabel('Frequency')
    for p in ax.patches:
        x = p.get_bbox().get_points()[:, 0]
        y = p.get_bbox().get_points()[1, 1]
        # Setting text alignment
        ax.annotate('{:.1f}%'.format(100.*y/ncount), (x.mean(), y),
                    ha='center', va='bottom')
    # Use aa LinearLocator to ensure the correct number of ticks
    ax.yaxis.set_major_locator(ticker.LinearLocator(11))
    # y-axis ticks
    ax2.yaxis.set_ticks(np.arange(0, 101, 10))
    ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f%%'))
    # Axes range
    ax2.set_ylim(0, 100)
    ax.set_ylim(0, ncount)
    # Use a MultipleLocator to ensure a ticker spacing of 10
    ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
    # Grid lines
    ax2.grid(None)
    
# Calculate correlation coefficients
def corrfunc(x, y, **kws):
    '''Calculate correlation coefficients.'''
    r, _ = stats.pearsonr(x, y)
    ax = plt.gca()
    ax.annotate("r = {:.2f}".format(r),
                xy=(.1, .6), xycoords=ax.transAxes,
                size=24)