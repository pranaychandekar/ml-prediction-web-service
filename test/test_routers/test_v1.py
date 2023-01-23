"""
v1.py test cases
 
Author - Pranay Chandekar
"""
import asyncio
import logging

import unittest
from unittest.mock import patch

from src.domain.request_response_schemas import PredictionServiceRequest

from src.routers.v1 import get_response


class TestV1(unittest.TestCase):
    logging.basicConfig(level=logging.FATAL)

    @patch("src.routers.v1.Logger")
    @patch("src.routers.v1.PredictionService")
    @patch("src.services.classifier.fasttext")
    def test_get_response(self, mock_fasttext, mock_prediction_service, mock_logger):
        prediction_service_request_json = {
            "source": "pytest",
            "text": "Don't let the knives sink :P"
        }
        prediction_service_request = PredictionServiceRequest.parse_obj(prediction_service_request_json)

        mock_prediction_service.get_response.return_value = {
            "label": "knives",
            "confidence": 86.64
        }

        mock_logger.get_instance.return_value = logging

        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(get_response(prediction_service_request))

        self.assertEqual(result.status_code, 200)