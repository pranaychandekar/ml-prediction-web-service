"""
Prediction Service
"""
from src.services.classifier import Classifier


class PredictionService:
    """
    This class runs the prediction and returns the response.

    :Author: Pranay Chandekar
    """

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
        response = {}

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
        prediction_result = Classifier().get_instance().predict(text)

        # Step 02: Parse the prediction result.
        predicted_label = str(prediction_result[0][0])
        predicted_label = predicted_label.replace("__label__", "").strip()
        confidence = round(100 * prediction_result[1][0], 2)

        # Step 03: Return the result.
        return predicted_label, confidence
