# Exercise 23.1 (World Bank data)
import matplotlib.pyplot as plt

from pandas_datareader import wb

data = wb.download(country=['DK', 'NO', 'SE', 'FI', 'IS'], indicator='SP.POP.TOTL', start=1950, end=2019)
data = data.unstack(level=0)
data.plot()
plt.show()

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html

# Exercise 24.1 (whiten)
from math import sqrt


def whiten(data):
    n = len(data)  # vektorer
    d = len(data[0])  # indgange i vektorne
    sum_ = [0] * d  # vektorsummer
    for obs in data:
        for i in range(len(obs)):
            sum_[i] += obs[i]

    mean = [x / n for x in sum_]  # gennemsnitter

    var = [0] * n  # vektorvarianser
    for obs in data:
        for i in range(len(obs)):
            var[i] += (obs[i] - mean[i]) ** 2

    return [[x / sqrt(v / n)
             for x, v in zip(obs, var)]
            for obs in data]

import numpy as np

def np_whiten(data):
    n = len(data)
    mean = np.sum(data, axis=0, keepdims=True) / n  # gennemsnitter
    var = np.sqrt(np.sum((data - mean)**2, axis=0, keepdims=True) / n)  # vektorvarianser
    return data / var

def np_whiten2(data):
    return data / np.std(data, axis=0, keepdims=True)

# Exercise 24.3* (k-means clustering in 1D)
def memoize(f):
    # answers[args] = f(*args)
    answers = {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper

def k_mean_1D_double_memoize(k, L):
    @memoize
    def one_cluster(i, j):
        ''' consider L[i:j] to be one cluster '''
        centroid = sum(L[i:j]) / (j - i)
        cost = sum((x - centroid)**2 for x in L[i:j])
        return cost, centroid

    @memoize
    def solve(k, n):
        ''' find k optimal centroids for L[0:n] '''
        cost, solution = one_cluster(0, n)

        if k > 1:
            for i in range(1, n-1):
                cost_head, solution_head = solve(k - 1, i)  # find k-1 centroids in the first i points
                cost_tail, solution_tail = one_cluster(i, n)  # while assuming the [i,n] points are a cluster
                                                                                   # we know that x_i <= x_{i + 1}
                cost_ = cost_tail + cost_head
                if cost_ < cost:                                           # continue with the best cut
                    cost = cost_
                    solution = (solution_head, solution_tail)
        return cost, solution

    L = sorted(L)
    return solve(k, len(L))