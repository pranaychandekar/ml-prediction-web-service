"""
app_configs.py test case
 
Author - Pranay Chandekar
"""
import unittest

from unittest.mock import patch

from src.configurations.app_configs import AppConfigs


class TestAppConfigs(unittest.TestCase):

    @patch("src.configurations.app_configs.json")
    @patch("src.configurations.app_configs.open")
    def test_(self, mock_open, mock_json):
        mock_json.load.return_value = {"PORT": 8080}

        configs = AppConfigs().get_instance()

        self.assertEqual(configs.get("PORT"), 8080)

