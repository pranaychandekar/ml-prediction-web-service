import os

from sanic import Sanic
from sanic import response
from sanic_openapi import doc
from sanic_openapi import swagger_blueprint

from src.configurations.configs import Configs

import time

app = Sanic()
app.blueprint(swagger_blueprint)

config_directory = "conf"
config_file_path = os.path.join(config_directory, "app.conf")

app.config.from_pyfile(config_file_path)

CONFIGS = Configs.get_instance(app)

from src.utils.logging_util import Logger
from src.utils.request_parser import RequestParser
from src.services.prediction_service import PredictionService

LOGGER = Logger.get_instance()


@app.route("/", methods=["GET"])
@doc.summary("Hit this end-point to check if service is up and running.")
async def index(request):
    """
    Use this end-point to check if the ml-prediction-web-service is up and running.

    :return: The success message if the service is up.
    """
    LOGGER.logger.info("Checking the service setup.\n")
    return response.json(
        {
            "status": 200,
            "service": "ml-prediction-web-service",
            "version": "1.0",
            "author": "Pranay Chandekar",
            "linkedIn": "https://www.linkedin.com/in/pranaychandekar/",
            "message": "The web service is up and running!",
        }
    )


@app.route("v1/predict", methods=["POST"])
@doc.summary(
    "Hit this end-point with a post request to predict the label for the text in the request."
)
@doc.consumes(
    doc.JsonBody({"source": str, "text": str}),
    location="body",
    content_type="application/json",
)
async def get_response(request):
    """
    This end point predicts the label for the given text and returns the result in the response.

    :param request: The request for the API.
    :return: The response with the prediction results.
    """
    tic = time.time()

    # Step 01: Set the default response.
    prediction_service_response = response.json(
        {
            "status": 400,
            "message": "Bad Request! Please ensure that the 'text' key is not empty.",
        }
    )

    try:
        # Step 02: Parse the incoming request.
        parsed_request = RequestParser.request_parser(request.json)

        LOGGER.logger.info(
            "Received request from source: "
            + parsed_request["source"]
            + " to predict the label for text: "
            + parsed_request["text"]
        )

        # Step 03: If the request is valid then trigger the classifier to predict the label.
        if parsed_request["text"] != "":
            prediction_service_response = response.json(
                PredictionService.get_response(parsed_request["text"])
            )

    except Exception as e:
        error = "Failed to predict label for " + request.json() + " with error: " + str(e)
        LOGGER.logger.exception(error)
        LOGGER.log_err.exception(error)
        prediction_service_response = response.json(
            {
                "status": 500,
                "message": "Error while predicting the label. Please check the web service logs for more details.",
            }
        )

    toc = time.time()

    LOGGER.logger.info(
        "Total time taken to respond: " + str(round(1000 * (toc - tic), 2)) + " ms.\n"
    )

    # Step 04: Return the response.
    return prediction_service_response


if __name__ == "__main__":
    LOGGER.logger.info("\nStarting the ml-prediction-web-service.\n")
    app.run(
        host=CONFIGS.get_configuration("SOCKET_HOST"),
        port=CONFIGS.get_configuration("PORT"),
        workers=CONFIGS.get_configuration("THREAD_POOL"),
    )
