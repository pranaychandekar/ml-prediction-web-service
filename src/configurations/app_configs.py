"""
Application Configurations
"""
import json
from src.domain.constants import APP_CONFIGS_PATH


class AppConfigs:
    """
    The instance of this class holds the web service configurations.

    :Author: Pranay Chandekar
    """

    __instance = None

    def __init__(self):
        """
        This method initializes the instance of the web service configurations.
        """
        with open(APP_CONFIGS_PATH) as configs_file:
            self.configurations: dict = json.load(configs_file)

        AppConfigs.__instance = self

    def get_configuration(self, configuration: str):
        """
        This method returns the requested configuration value.

        :param configuration: The name of the configuration.
        :return: The configuration value.
        """
        return self.configurations.get(configuration)

    @staticmethod
    def get_instance():
        """
        This method returns an instance of the web service configurations.

        :return: The instance of the service configurations.
        """
        if AppConfigs.__instance is None:
            AppConfigs()
        return AppConfigs.__instance
