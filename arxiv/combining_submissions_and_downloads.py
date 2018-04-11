# -*- coding: utf-8 -*-

# arXiv Monthly Submissions & Downloads

# The usual suspects ...
import pandas as pd
import glob as gb

# Getting the data
downloads = pd.concat([pd.read_csv(file)
                       for file in 
                       gb.glob('*_downloads_*.csv')
                      ])
submissions = pd.concat([pd.read_csv(file)
                         for file in
                         gb.glob('*_submissions_*.csv')
                        ])
data = pd.merge(submissions, downloads, on='month')

# Create the new dataset
data.to_csv('combined_submissions_and_downloads.csv', sep=',')