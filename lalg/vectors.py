import numpy as np

"""
This file contains various functions to generate vectors of all kinds
"""


def nvect(low=0, high=5, size=(3, 1)):
    return np.random.random_integers(low, high, size)
