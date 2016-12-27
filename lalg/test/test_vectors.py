import unittest
import numpy as np
from lalg import *


class TestVectors(unittest.TestCase):

    def test_nvect_default_size(self):
        """
        Test default nvect() size
        """
        self.assertEqual(nvect().size, 3)

    def test_nvect_default_range(self):
        """
        Test default nvect() range
        """
        self.assertTrue(np.sum(nvect()) > 0)

    def test_easy_good_dim(self):
        """
        Test easy shaping of array
        """
        newArray = [1, 2, 3, 4, 5, 6]
        row = 2
        col = 3
        self.assertTrue(easy_vect(newArray, row, col).shape == (row, col))

if __name__ == '__main__':
    unittest.main()
