from sanic import Sanic


class Configs:
    """
    The instance of this class holds the ml-prediction-web-service configurations.

    :Author: Pranay Chandekar
    """

    __instance: Sanic = None

    def __init__(self, app: Sanic):
        """
        This method initializes the instance of the ml-prediction-web-service configurations.

        :param app: The Sanic instance.
        """
        self.configurations = app.config

        Configs.__instance = self

    def get_configuration(self, configuration: str):
        """
        This method returns the requested configuration value.

        :param configuration: The name of the configuration.
        :return: The configuration value.
        """
        return self.configurations.get(configuration)

    @staticmethod
    def get_instance(app: Sanic = None):
        """
        This method returns an instance of the ml-prediction-web-service configurations.

        :return: The instance of the service configurations.
        """
        if Configs.__instance is None:
            Configs(app)
        return Configs.__instance
