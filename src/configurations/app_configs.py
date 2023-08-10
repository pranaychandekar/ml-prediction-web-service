"""
Application Configurations
"""
import json

from src.domain.constants import APP_CONFIGS_PATH
from src.utils.singleton import Singleton


class AppConfigs(metaclass=Singleton):
    """
    The instance of this class holds the web service configurations.

    :Author: Pranay Chandekar
    """

    def __init__(self):
        """
        This method initializes the instance of the web service configurations.
        """
        with open(APP_CONFIGS_PATH, encoding="utf-8") as configs_file:
            self._configurations: dict = json.load(configs_file)

    def get_instance(self):
        """
        This method returns the AppConfigs instance

        :return: AppConfigs instance
        """
        return self._configurations
