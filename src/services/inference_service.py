from src.services.classifier import Classifier
from src.configurations.configs import Configs
from src.utils.logging_util import Logger

CONFIGS = Configs.get_instance()
LOGGER = Logger.get_instance()


class InferenceService:
    """
    This class runs the inference logic and returns the response.

    :Authors: pranaychandekar
    """

    __model = Classifier.get_instance().get_model()

    @staticmethod
    def get_response(text: str):
        """
        This method predicts the minimum overall experience required for a job.

        :param text: The text to be classified.
        :type text: str
        :return: The response containing the inference result.
        :rtype: dict
        """
        # Step 01: Initialize the response.
        response = dict()
        results = dict()

        # Step 02: Predict the label/class of the received text.
        inference_result = InferenceService.__model.predict(text)

        # Step 03: Parse the inference result.
        inferred_label = str(inference_result[0][0])
        inferred_label = inferred_label.replace("__label__", "").strip()
        confidence = round(100 * inference_result[1][0], 2)

        # Step 04: Prepare the response.
        results["label"] = inferred_label
        results["confidence"] = confidence
        response["status"] = 200
        response["results"] = results

        # Step 05: Return the response.
        return response
