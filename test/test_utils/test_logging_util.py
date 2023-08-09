"""
logging_util.py test cases
 
Author - Pranay Chandekar
"""
import unittest

from src.utils.logging_util import Logger


class TestLogger(unittest.TestCase):

    def test_get_instance(self):
        result = Logger().instance
        self.assertEqual(result, Logger().instance)

