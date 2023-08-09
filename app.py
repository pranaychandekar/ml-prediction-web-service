"""
Controller
"""
import uvicorn

from fastapi import FastAPI

from src.utils.logging_util import Logger
from src.configurations.app_configs import AppConfigs
from src.domain.constants import SOCKET_HOST, PORT
from src.domain.request_response_schemas import BuildResponse
from src.routers import v1

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


@app.get("/", tags=["Build"], response_model=BuildResponse)
async def build():
    """
    Hit this API to get build details.

    :return: The build details
    """
    Logger().get_instance().info("Checking the service setup.\n")
    return {
        "service": "ml-prediction-web-service",
        "version": "2.0",
        "author": "Pranay Chandekar",
        "linkedIn": "https://www.linkedin.com/in/pranaychandekar/",
        "message": "The web service is up and running!",
    }

app.include_router(v1.router, prefix="/v1")

if __name__ == "__main__":
    Logger().get_instance().info("Starting the web service.")
    uvicorn.run(
        app,
        host=AppConfigs().get_instance().get(SOCKET_HOST),
        port=AppConfigs().get_instance().get(PORT),
    )
