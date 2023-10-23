from fastapi.testclient import TestClient

from application import app

client = TestClient(app)


def test_build():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == 200
