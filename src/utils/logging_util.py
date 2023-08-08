"""
Logging Util
"""
import json
import logging
import logging.config

from src.domain.constants import LOGGING_CONFIGS_PATH
from src.utils.singleton import Singleton


class Logger(metaclass=Singleton):
    """
    This is a utility to write the web service logs.

    :Author: Pranay Chandekar
    """

    def __init__(self):
        """
        This method initialized the Logger utility.
        """
        logging.config.dictConfig(Logger.get_log_configs_dict())

        self.instance = logging.getLogger("fileLogger")

    @staticmethod
    def get_log_configs_dict():
        """
        This method reads the logging configs from a json file
        and returns it as a dictionary.

        :return: configs dictionary
        """
        with open(LOGGING_CONFIGS_PATH) as config_file:
            configs_dict = json.load(config_file)
        return configs_dict

    def get_instance(self):
        """
        This method returns an instance of the Logger utility.

        :return: The Logger utility instance.
        """
        return self.instance
