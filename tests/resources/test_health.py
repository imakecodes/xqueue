from fastapi.testclient import TestClient

from app import __version__
from app.main import app

client = TestClient(app)


def test_get_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"version": __version__}


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello messengers"}
