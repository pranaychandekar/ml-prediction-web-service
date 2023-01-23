"""
Prediction Service End Point
"""
import time

from fastapi.routing import APIRouter
from src.utils.logging_util import Logger
from src.domain.request_response_schemas import (
    PredictionServiceRequest,
    PredictionServiceResponse,
)
from src.services.prediction_service import PredictionService

router = APIRouter()


@router.post(
    "/predict", tags=["Prediction Service"], response_model=PredictionServiceResponse
)
async def get_response(request: PredictionServiceRequest):
    """
    This end point predicts the label for the given text and returns the result in the response.

    :param request: The request for the API.

    :return: The response with the prediction results.
    """
    tic = time.time()
    Logger.get_instance().info("Request: %s", request.json())
    prediction_service_response = PredictionService.get_response(request.text)
    Logger.get_instance().info(
        "Total time taken to respond: %s ms.\n", round(1000 * (time.time() - tic), 2)
    )
    return prediction_service_response
