import unittest
from unittest.case import TestCase

def multiply(x,y):

    return x*y

class TestMultiply(unittest.TestCase):

    def test(self):
        self.assertEqual(multiply((32-32),5/9),0)

if __name__ == '__main__':
    unittest.main()