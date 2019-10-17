import logging
import logging.config

from src.configurations.configs import Configs

CONFIGS = Configs.get_instance()


class Logger:
    """
    This is a utility to write the web service logs.

    :Author: Pranay Chandekar
    """

    __instance = None

    def __init__(self):
        """
        This method initialized the Logger utility.
        """
        path = CONFIGS.get_configuration("LOG_CONFIG_PATH")

        logging.config.fileConfig(path)

        self.logger = logging.getLogger("fileLogger")
        self.log_err = logging.getLogger("errLogger")

        Logger.__instance = self

    @staticmethod
    def get_instance():
        """
        This method returns an instance of the Logger utility.

        :return: The Logger utility instance.
        """
        if Logger.__instance is None:
            Logger()
        return Logger.__instance
