#!/usr/bin/env python

import numpy as np

"""
This file contains various functions to generate vectors of all kinds
"""


def nvect(low=0, high=5, size=(3, 1)):
    """Create random vector

    Parameters
    ----------
    low : integer
        Lower range of numbers allowed in vector

    high : integer
        Upper range of numbers allowed in vector

    size : tuple
        Tuple governing the size of the matrix

    Returns
    -------
    self : ndarray
        Array constrained by range of numbers and size

    Examples
    --------
    >>> lalg.nvect()
    >>> lalg.nvect(2)
    >>> lalg.nvect(1, 10)
    >>> lalg.nvect(1, 5, (3, 3))
    """
    return np.random.randint(low, high, size)


def easy_vect(inArray, row, col):
    """Create easy vector from array and size

    Parameters
    ----------
    inArray : ndarray
        Column/row vector

    row : integer
        Number of rows wanted in array

    col : integer
        Number of columns wanted in array

    Returns
    -------
    self : ndarray
        Array reshaped based on parameters

    Examples
    --------
    >>> import numpy as np
    >>> lalg.easy_vect(np.array([1, 2, 3, 4]), 2, 2)
    >>> lalg.easy_vect(np.array([1, 2, 3, 4, 5, 6]), 2, 3)
    >>> lalg.easy_vect(np.array([1, 2, 3, 4, 5, 6]), 3, 2)
    """
    return np.array(inArray).reshape(row, col)
