from utils.logging_util import Logger

LOGGER = Logger.get_instance()


class RequestParser:
    """
    The objective of this class is to parse the request received by the ml-prediction-web-service.

    :Author: Pranay Chandekar
    """

    @staticmethod
    def request_parser(request: dict):
        """
        This method parses the request received by the ml-prediction-web-service.

        :param request: The received request.
        :type request: dict
        :return: The parsed request.
        :rtype: dict
        """

        parsed_request = dict()

        if "source" not in request or request["source"] is None:
            error = "source is missing"
            LOGGER.logger.exception(error)
            LOGGER.log_err.exception(error)
            parsed_request["source"] = ""
        else:
            parsed_request["source"] = str(request["source"]).strip()

        if "text" not in request or request["text"] is None:
            error = "text is missing"
            LOGGER.logger.exception(error)
            LOGGER.log_err.exception(error)
            parsed_request["text"] = ""
        else:
            parsed_request["text"] = str(request["text"]).strip()

        return parsed_request
