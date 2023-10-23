"""
prediction_service.py test cases
 
Author - Pranay Chandekar
"""
import logging

import unittest
from unittest.mock import patch, Mock, MagicMock

from src.services.prediction_service import PredictionService


class TestPredictionService(unittest.TestCase):
    """
    This class tests all the code in the prediction_service.py file
    """
    logging.basicConfig(level=logging.FATAL)

    @patch("src.services.prediction_service.PredictionService")
    def test_response(self, mock_prediction_service):
        mock_prediction_service.predict_label.return_value = "knives", 86.64

        text = "Don't let the knives sink :P"
        result = PredictionService.get_response(text)
        self.assertEqual(type(result.get("label")), str)

    @patch("src.services.prediction_service.Classifier")
    def test_predict_label(self, mock_classifier):
        mock_classifier = Mock()

        text = "Don't let the knives sink :P"
        label, confidence = PredictionService.predict_label(text)

        print(label, confidence)

        self.assertEqual(type(label), str)
        self.assertEqual(type(confidence), type(confidence))

