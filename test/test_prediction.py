import json

import pytest
from sanic.websocket import WebSocketProtocol

from src import prediction

my_app = prediction.app


@pytest.yield_fixture
def app():
    yield my_app


@pytest.fixture
def test_cli(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app, protocol=WebSocketProtocol))


async def test_index_status(test_cli):
    resp = await test_cli.get("/")
    out = await resp.json()

    assert resp.status == 200
    assert out["message"] == "The web service is up and running!"


async def test_checkpost(test_cli):
    req_input = {
            "source": "testCase",
            "text": "Why not put knives in the dishwasher?"
        }
    resp = await test_cli.post("v1/predict", data=json.dumps(req_input))
    print(resp)
    print(resp.status)
    assert resp.status == 200
