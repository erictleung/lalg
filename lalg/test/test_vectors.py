import unittest
from lalg import *

class TestVectors(unittest.TestCase):

    def test_nvect_default(self):
        self.assertEqual(nvect().size, 3)

if __name__ == '__main__':
    unittest.main()
