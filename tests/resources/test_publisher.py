from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_post_message():
    response = client.post("/publish/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"msg": "Received"}
