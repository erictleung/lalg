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

if __name__ == '__main__':
    unittest.main()
