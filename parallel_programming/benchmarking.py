# -*- coding: utf-8 -*-
'''
Sample data and `timeit` benchmarks.
'''

from scipy.stats import multivariate_normal
from matplotlib import pyplot as plt
import numpy as np
import multiprocessing as mp
import timeit
import platform

np.random.seed(123)

# Generate random 2D-patterns
mu_vec = np.array([0, 0])
cov_mat = np.array([[1, 0], [0, 1]])
x_2Dgauss = np.random.multivariate_normal(mu_vec, cov_mat, 10000)
var = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]])
print('Actual probability density:{}'.format(var.pdf([0, 0])))

#def parzen_estimation(x_samples, point_x, h):
#    '''
#    Implementation of a hypercube kernel for Parzen-window estimation.
#
#    Keyword arguments:
#        - x_sample  : training sample, 1-dimensional numpy array
#        - x         : point x for density estimation, 1-dimensional numpy array
#        - h         : window width
#
#    Returns the predicted pdf as float.
#    '''
#    k_n = 0
#    for row in x_samples:
#        x_i = (point_x - row[:, np.newaxis]) / (h)
#        for row in x_i:
#            if np.abs(row) > (1/2):
#                break
#        else:
#            k_n += 1
#    return (k_n / len(x_samples)) / (h**point_x.shape[1])
#
#def serial(samples, x, widths):
#    return [parzen_estimation(samples, x, w) for w in widths]
#
#def multiprocess(processes, samples, x, widths):
#    pool = mp.Pool(processes=processes)
#    results = [pool.apply_async(parzen_estimation, args=(samples, x, w)) for w in widths]
#    results = [p.get() for p in results]
#    results.sort()
#    return results

def print_sysinfo():
    print('\nPython version  :', platform.python_version())
    print('compiler        :', platform.python_compiler())
    print('\nsystem     :', platform.system())
    print('release    :', platform.release())
    print('machine    :', platform.machine())
    print('processor  :', platform.processor())
    print('CPU count  :', mp.cpu_count())
    print('interpreter:', platform.architecture()[0])
    print('\n\n')

def plot_results():
    bar_labels = ['serial', '2', '3', '4', '6']
    fig = plt.figure(figsize=(10,8))

    # plot bars
    y_pos = np.arange(len(benchmarks))
    plt.yticks(y_pos, bar_labels, fontsize=16)
    bars = plt.barh(y_pos, benchmarks,
             align='center', alpha=0.4, color='g')

    # annotation and labels

    for ba,be in zip(bars, benchmarks):
        plt.text(ba.get_width() + 2, ba.get_y() + ba.get_height()/2,
                '{0:.2%}'.format(benchmarks[0]/be),
                ha='center', va='bottom', fontsize=12)

    plt.xlabel('time in seconds for n=%s' %n, fontsize=14)
    plt.ylabel('number of processes', fontsize=14)
    t = plt.title('Serial vs. Multiprocessing via Parzen-window estimation', fontsize=18)
    plt.ylim([-1,len(benchmarks)+0.5])
    plt.xlim([0,max(benchmarks)*1.1])
    plt.vlines(benchmarks[0], -1, len(benchmarks)+0.5, linestyles='dashed')
    plt.grid()

    plt.show()

widths = np.linspace(1.0, 1.2, 100)
benchmarks = list()
PointX = np.array([[0], [0], [0]])
benchmarks.append(timeit.Timer('serial(x_2Dgauss, PointX, widths)',
            'from __main__ import serial, x_2Dgauss, PointX, widths').timeit(number=1))
benchmarks.append(timeit.Timer('multiprocess(2, x_2Dgauss, PointX, widths)',
            'from __main__ import multiprocess, x_2Dgauss, PointX, widths').timeit(number=1))
benchmarks.append(timeit.Timer('multiprocess(3, x_2Dgauss, PointX, widths)',
            'from __main__ import multiprocess, x_2Dgauss, PointX, widths').timeit(number=1))
benchmarks.append(timeit.Timer('multiprocess(4, x_2Dgauss, PointX, widths)',
            'from __main__ import multiprocess, x_2Dgauss, PointX, widths').timeit(number=1))
benchmarks.append(timeit.Timer('multiprocess(5, x_2Dgauss, PointX, widths)',
            'from __main__ import multiprocess, x_2Dgauss, PointX, widths').timeit(number=1))
benchmarks.append(timeit.Timer('multiprocess(6, x_2Dgauss, PointX, widths)',
            'from __main__ import multiprocess, x_2Dgauss, PointX, widths').timeit(number=1))

plot_results()
print_sysinfo()
