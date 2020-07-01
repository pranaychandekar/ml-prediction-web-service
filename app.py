"""
Controller
"""
import time
import uvicorn

from fastapi import FastAPI

from src.utils.logging_util import Logger
from src.configurations.app_configs import AppConfigs
from src.domain.constants import SOCKET_HOST, PORT
from src.domain.request_response_schemas import (
    BuildResponse,
    PredictionServiceRequest,
    PredictionServiceResponse,
)
from src.services.prediction_service import PredictionService

tags_metadata = [
    {"name": "Build", "description": "Use this API to check project build number."},
    {
        "name": "Prediction Service",
        "description": "Prediction Service APIs",
        "externalDocs": {
            "description": "External Document",
            "url": "https://link.to.external.document.com/",
        },
    },
]

app = FastAPI(
    title="ML Prediction Web Service",
    description="This project is a production ready ML Prediction Web Service template. "
                "<br /><br />"
                "Author - [***Pranay Chandekar***](https://www.linkedin.com/in/pranaychandekar/)",
    version="2.0.0",
    openapi_tags=tags_metadata,
    docs_url="/swagger/",
)
LOGGER = Logger.get_instance()
APP_CONFIGS = AppConfigs.get_instance()


@app.get("/", tags=["Build"], response_model=BuildResponse)
async def build():
    """
    Hit this API to get build details.

    :return: The build details
    """
    LOGGER.logger.info("Checking the service setup.\n")
    return {
        "service": "ml-prediction-web-service",
        "version": "2.0",
        "author": "Pranay Chandekar",
        "linkedIn": "https://www.linkedin.com/in/pranaychandekar/",
        "message": "The web service is up and running!",
    }


@app.post(
    "/v1/predict", tags=["Prediction Service"], response_model=PredictionServiceResponse
)
async def get_response(request: PredictionServiceRequest):
    """
    This end point predicts the label for the given text and returns the result in the response.

    :param request: The request for the API.

    :return: The response with the prediction results.
    """
    tic = time.time()
    LOGGER.logger.info("Request: %s", request.json())
    prediction_service_response = PredictionService.get_response(request.text)
    LOGGER.logger.info(
        "Total time taken to respond: %s ms.\n", round(1000 * (time.time() - tic), 2)
    )
    return prediction_service_response


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=APP_CONFIGS.get_configuration(SOCKET_HOST),
        port=APP_CONFIGS.get_configuration(PORT),
    )
