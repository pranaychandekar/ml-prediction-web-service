import time
import uvicorn

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from utils.logging_util import Logger
from configurations.app_configs import AppConfigs
from domain.request import Request
from services.prediction_service import PredictionService

app = FastAPI()
LOGGER = Logger.get_instance()
APP_CONFIGS = AppConfigs.get_instance()


@app.get("/")
async def index():
    """
    Use this end-point to check if the ml-prediction-web-service is up and running.

    :return: The success message if the service is up.
    """
    LOGGER.logger.info("Checking the service setup.\n")
    return JSONResponse(
        {
            "status": 200,
            "service": "ml-prediction-web-service",
            "version": "1.0",
            "author": "Pranay Chandekar",
            "linkedIn": "https://www.linkedin.com/in/pranaychandekar/",
            "message": "The web service is up and running!",
        }
    )


@app.post("/v1/predict")
async def get_response(request: Request):
    """
    This end point predicts the label for the given text and returns the result in the response.

    :param request: The request for the API.
    :return: The response with the prediction results.
    """
    tic = time.time()

    # Step 01: Set the default response.
    prediction_service_response = {
        "status": 400,
        "message": "Bad Request! Please ensure that the 'text' key is not empty.",
    }

    try:
        LOGGER.logger.info(
            "Received request from source: "
            + request.source
            + " to predict the label for text: "
            + request.text
        )

        # Step 02: If the request is valid then trigger the classifier to predict the label.
        if request.text != "":
            prediction_service_response = PredictionService.get_response(request.text)

    except Exception as e:
        error = (
            "Failed to predict label for " + request.json() + " with error: " + str(e)
        )
        LOGGER.logger.exception(error)
        LOGGER.log_err.exception(error)
        prediction_service_response = {
            "status": 500,
            "message": "Error while predicting the label. Please check the web service logs for more details.",
        }

    toc = time.time()

    LOGGER.logger.info(
        "Total time taken to respond: " + str(round(1000 * (toc - tic), 2)) + " ms.\n"
    )

    # Step 03: Return the response.
    return JSONResponse(content=prediction_service_response)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=APP_CONFIGS.get_configuration("SOCKET_HOST"),
        port=APP_CONFIGS.get_configuration("PORT"),
    )
