"""
Prediction Service End Point
"""
from fastapi.routing import APIRouter

from src.utils.logging_util import Logger, log_execution_time
from src.domain.request_response_schemas import (
    PredictionServiceRequest,
    PredictionServiceResponse,
)
from src.services.prediction_service import PredictionService

router = APIRouter()


@router.post(
    "/predict", tags=["Prediction Service"], response_model=PredictionServiceResponse
)
@log_execution_time
async def get_response(request: PredictionServiceRequest):
    """
    This end point predicts the label for the given text and returns the result in the response.

    :param request: The request for the API.

    :return: The response with the prediction results.
    """
    Logger().get_instance().info("Request: %s", request.json())
    return PredictionService.get_response(request.text)
