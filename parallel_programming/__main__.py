# -*- coding: utf-8 -*-
'''
Everything we need ...
'''
from scipy.stats import multivariate_normal
import numpy as np
import multiprocessing as mp

mu_vec = np.array([0, 0])
cov_mat = np.array([[1, 0], [0, 1]])
x_2Dgauss = np.random.multivariate_normal(mu_vec, cov_mat, 10000)
var = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]])
print('Actual probability density:{}'.format(var.pdf([0, 0])))

def parzen_estimation(x_samples, point_x, h):
    k_n = 0
    for row in x_samples:
        x_i = (point_x - row[:,np.newaxis]) / (h)
        for row in x_i:
            if np.abs(row) > (1/2):
                break
        else: # "completion-else"*
            k_n += 1
    return (h, (k_n / len(x_samples)) / (h**point_x.shape[1]))

def serial(samples, x, widths):
    return [parzen_estimation(samples, x, w) for w in widths]

def multiprocess(processes, samples, x, widths):
    pool = mp.Pool(processes=processes)
    results = [pool.apply_async(parzen_estimation, args=(samples, x, w)) for w in widths]
    results = [p.get() for p in results]
    results.sort() # to sort the results by input window width
    return results
