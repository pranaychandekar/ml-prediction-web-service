"""
logging_util.py test cases
 
Author - Pranay Chandekar
"""
import unittest

from src.utils.logging_util import Logger


class TestLogger(unittest.TestCase):

    def test_get_instance(self):
        result = Logger().get_instance()
        self.assertEqual(result, Logger().get_instance())

