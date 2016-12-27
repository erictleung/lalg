import numpy as np

"""
This file contains various functions to generate vectors of all kinds
"""


def nvect(low=0, high=5, size=(3, 1)):
    """
    Create random vector
    """
    return np.random.randint(low, high, size)


def easy_vect(inArray, row, col):
    """
    Create easy vector from array and size
    """
    return np.array(inArray).reshape(row, col)
