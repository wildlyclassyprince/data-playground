# -*- coding: utf-8 -*-

'''
arXiv Monthly Submissions & Downloads
-------------------------------------

This script takes the submissions and downloads files, and
merges (right-join) them into a single file by pivoting on
the month (i.e., the date corresponding to the number of
submissions or downloads on that month).

'''

# The usual suspects ...
import glob as gb
import pandas as pd

# Getting the data
DOWNLOADS = pd.concat([pd.read_csv(file)
                       for file in
                       gb.glob('*_downloads_*.csv')
                      ])
SUBMISSIONS = pd.concat([pd.read_csv(file)
                         for file in
                         gb.glob('*_submissions_*.csv')
                        ])
DATA = pd.merge(SUBMISSIONS, DOWNLOADS, on='month')

# Create the new dataset
DATA.to_csv('combined_submissions_and_downloads.csv', sep=',')
