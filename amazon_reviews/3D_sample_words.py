# -*- coding: utf-8 -*-
# the usual suspects ...
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, plot, iplot
from plotly import __version__

print(__version__)

# getting the data
data = pd.read_csv('...amazon_reviews/sample_after_training.csv', index_col = ['Unnamed: 0'])
#labels = pd.read_csv('.../amazon_reviews/labels.csv')

x, y, z = data.list_1, data.list_2, data.list_3
trace_1 = go.Scatter3d(
    x = x,
    y = y,
    z = z,
    hovertext = data.word,
    mode = 'markers',
    marker = dict(
        size = 5,
        color = data.sentiment,
        colorscale = 'Virdis',
        opacity = 0.8,
        line = dict(
            width = 1),
        showscale = True,
        colorbar = dict(title = 'Distance'))
)
data = [trace_1]
layout = go.Layout(
    title = 'Word Embeddings',
    scene = dict(xaxis=dict(title=''),
                 yaxis=dict(title=''),
                 zaxis=dict(title=''),
                ),
    margin = dict(
        l = 0,
        r = 0,
        b = 0,
        t = 0)
)
fig = go.Figure(data = data, layout = layout,)
plot(fig)
