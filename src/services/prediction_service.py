from services.classifier import Classifier
from configurations.app_configs import AppConfigs
from utils.logging_util import Logger

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
        results = dict()

        # Step 02: Predict the label/class of the received text.
        prediction_result = PredictionService.__model.predict(text)

        # Step 03: Parse the prediction result.
        predicted_label = str(prediction_result[0][0])
        predicted_label = predicted_label.replace("__label__", "").strip()
        confidence = round(100 * prediction_result[1][0], 2)

        # Step 04: Prepare the response.
        results["label"] = predicted_label
        results["confidence"] = confidence
        response["status"] = 200
        response["results"] = results

        # Step 05: Return the response.
        return response
