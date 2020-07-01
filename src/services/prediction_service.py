"""
Prediction Service
"""
from src.services.classifier import Classifier
from src.configurations.app_configs import AppConfigs
from src.utils.logging_util import Logger

APP_CONFIGS = AppConfigs.get_instance()
LOGGER = Logger.get_instance()


class PredictionService:
    """
    This class runs the prediction and returns the response.

    :Author: Pranay Chandekar
    """

    __model = Classifier.get_instance().get_model()

    @staticmethod
    def get_response(text: str):
        """
        This method performs the prediction and prepares the response.

        :param text: The text to be classified.
        :type text: str
        :return: The response containing the prediction result.
        :rtype: dict
        """
        # Step 01: Initialize the response.
        response = dict()

        # Step 02: Prepare the response.
        response["label"], response["confidence"] = PredictionService.predict_label(
            text
        )

        # Step 03: Return the response.
        return response

    @staticmethod
    def predict_label(text: str):
        """
        This method uses the classification model to predict the label.

        :param text: The text to be classified.
        :return: the predicted label and the confidence
        """
        # Step 01: Predict the label
        prediction_result = PredictionService.__model.predict(text)

        # Step 02: Parse the prediction result.
        predicted_label = str(prediction_result[0][0])
        predicted_label = predicted_label.replace("__label__", "").strip()
        confidence = round(100 * prediction_result[1][0], 2)

        # Step 03: Return the result.
        return predicted_label, confidence
