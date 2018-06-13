# -*- coding: utf-8 -*-

# The suspects ...
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

# Information
__author__ = "wildlyclassyprince"
__version__ = "$Revision: 0.1.1 $"
__date__ = "$Date: Wed Jun 13 15:50:36 CAT 2018 $"
__licence__ = "GNU"

# Value counts
def unique_value_counts(dataframe):
	'''
	Prints the unique value counts for each column.
	'''
	_cols = (x for x in dataframe.columns)
	try:
		while True:
			field = _cols.__next__()
			print('='*75,
				  '\n Column Name: ', field,
				  '\n\n', dataframe[field].unique(),
				  '\n',
				  '='*75,
				  '\n')
	except StopIteration:
		print('Done.')
	except KeyError:
		print('Nothing to do.\n')

# Letter-case
def word_case(dataframe, font='Title'):
	'''
	Change the letter-case for columns containing string.
	'''
	_names = (i for i in dataframe.columns)
	try:
		while True:
			column = _names.__next__()
			if (dataframe[column].dtype == 'O'):
				if (font.lower() == 'title'):
					dataframe[column] = dataframe[column].str.title()
				elif (font.lower() == 'lower'):
					dataframe[column] = dataframe[column].str.lower()
				elif (font.lower() == 'upper'):
					dataframe[column] = dataframe[column].str.upper()
				elif (font.lower() == 'sentence'):
					dataframe[column] = dataframe[column].str.capitalize()
				else:
					pass
	except StopIteration:
		print('Done.\n')
	except KeyError:
		print('Nothing to do.\n')
	return dataframe.head()

# Removing specific columns
def drop_fields(fields, dataframe):
	'''
	Returns the dataframe after deleting the tagged columns.
	'''
	print('Initial dataframe shape: {}\n'.format(dataframe.shape))
	_drop = (x for x in fields)
	try:
		while True:
			del dataframe[_drop.__next__()]
	except StopIteration:
		print('\nDone!\nNew dataframe shape: {}\n\nThis is what the dataframe looks like now:\n'.format(dataframe.shape))
	except KeyError:
		print('Column does not exist.')
		pass
	return dataframe.head()


# Removing redundant columns
def remove_columns(dataframe):
	'''
	To remove redundant columns, i.e., columns with single or no entries,
	or with more than 50% of the data missing.
	'''
	# First, we identify the columns we want to remove:
	print('Initial shape of the dataset:{}\n'.format(dataframe.shape))
	_removeColumn = []
	for column in dataframe.columns:
		# 1. Number of unique items the columns contains:
		if (len(dataframe[column].unique()) == 1):
			_removeColumn.append(column)
		# 2. Number of missing values:
		elif (dataframe[column].isnull().sum() > ((dataframe.shape[0])/2)):
			_removeColumn.append(column)

	if (len(_removeColumn) > 0):
		for column in _removeColumn:
			print('The following will be removed: {}\n'.format(column))
	else:
		print('Nothing to delete.\n')

	# Removing the columns
	deleteColumn = (x for x in _removeColumn)
	try:
		while True:
			del dataframe[deleteColumn.__next__()]
	except StopIteration:
		print('Final shape of the dataset:{}'.format(dataframe.shape))

	return dataframe.head()

# Frequency plot
def frequency_plot(dataframe, x, title, xlabel, hue=None):
    # Plot settings
    plt.rcParams['figure.figsize'] = (16.0, 9.0)
    # Size of dataframe
    ncount=len(dataframe)
    # Our default chart
    ax=sns.countplot(data=dataframe, x=x, hue=hue)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel)
    # Making the twin axes
    ax2=ax.twinx()
    # Switching axes so that percentage is on the left and frequency on the right
    ax2.yaxis.tick_left()
    ax.yaxis.tick_right()
    # We also need to switch the labels
    ax.yaxis.set_label_position('right')
    ax2.yaxis.set_label_position('left')
    # Labelling our axes
    ax2.set_ylabel('Percentage')
    ax.set_ylabel('Frequency Count')
    for p in ax.patches:
        x=p.get_bbox().get_points()[:,0]
        y=p.get_bbox().get_points()[1,1]
        # Setting text alignment
        ax.annotate('{:.1f}%'.format(100.*y/ncount), (x.mean(), y), ha='center', va='bottom')
    # Use a LinearLocator to ensure the correct number of ticks
    ax.yaxis.set_major_locator(ticker.LinearLocator(11))
    # Setting the y-axis ticks
    ax2.yaxis.set_ticks(np.arange(0, 101, 10))
    ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f%%'))
    # Setting the axes range
    ax2.set_ylim(0, 100)
    ax.set_ylim(0, ncount)
    # Use a MultipleLocator to ensure a tick spacing of 10
    ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
    # Grid lines
    ax2.grid(None)
