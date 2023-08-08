"""
Classifier Singleton
"""
import fasttext as ft

from src.domain.constants import MODEL_PATH
from src.configurations.app_configs import AppConfigs
from src.utils.logging_util import Logger


class Classifier:
    """
    This class is a singleton which returns the instance of the Classifier.

    :Author: Pranay Chandekar
    """

    __instance = None

    def __init__(self):
        """
        This method initializes the instance of the Classifier.
        """
        if Classifier.__instance is not None:
            Logger().get_instance().exception("This class is a singleton!")
        else:
            self.model = False
            self.load_model()

    def load_model(self):
        """
        This method loads the Classifier model in the instance variable 'model'.
        """
        # Step 01: Load the model path from the configurations.
        model_path = AppConfigs.get_instance().get(MODEL_PATH)

        # Step 02: Load the model.
        self.model = ft.load_model(model_path)

        # Step 03: Assign this instance to '__instance'.
        Classifier.__instance = self

        Logger().get_instance().info(
            "Finished loading the classifier model: %s", self.get_model()
        )

    def get_model(self):
        """
        This method returns the Classifier model.

        :return: The Classifier model.
        """
        return self.model

    @staticmethod
    def get_instance():
        """
        This method instantiates an instance of the Classifier
        if it is not already instantiated and returns the same.

        :return: - Instance of the Classifier
        """
        if Classifier.__instance is None:
            Classifier()
        return Classifier.__instance
