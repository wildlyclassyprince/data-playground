# -*- coding: utf-8 -*-
'''
Kernel density estimation for probability density functions using
the Parzen-window technique.
'''

import numpy as np

def parzen_estimation(x_samples, point_x, h):
    '''
    Implementation of a hypercube kernel for Parzen-window estimation.

    Keyword arguments:
        - x_sample  : training sample, 1-dimensional numpy array
        - x         : point x for density estimation, 1-dimensional numpy array
        - h         : window width

    Returns the predicted pdf as float.
    '''
    k_n = 0
    for row in x_samples:
        x_i = (point_x - row[:, np.newaxis]) / (h)
        for row in x_i:
            if np.abs(row) > (1/2):
                break
        else:
            k_n += 1
    return (k_n / len(x_samples)) / (h**point_x.shape[1])

# samples within the cube
X_inside = np.array([[0,0,0],[0.2,0.2,0.2],[0.1, -0.1, -0.3]])

X_outside = np.array([[-1.2,0.3,-0.3],[0.8,-0.82,-0.9],[1, 0.6, -0.7],
                      [0.8,0.7,0.2],[0.7,-0.8,-0.45],[-0.3, 0.6, 0.9],
                      [0.7,-0.6,-0.8]])

PointX = np.array([[0], [0], [0]])
X_all = np.vstack((X_inside, X_outside))
print('p(x) = {}'.format(parzen_estimation(X_all, PointX, h=1)))