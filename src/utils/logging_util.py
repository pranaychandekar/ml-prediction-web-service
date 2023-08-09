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
        with open(LOGGING_CONFIGS_PATH) as config_file:
            configs_dict = json.load(config_file)

        logging.config.dictConfig(configs_dict)

        self._instance = logging.getLogger("fileLogger")

    def get_instance(self):
        """
        This method returns the AppConfigs instance

        :return: Logger instance
        """
        return self._instance
