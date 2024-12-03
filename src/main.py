
import pytest
from fastapi.testclient import TestClient
from src.main import app

def client():
    return TestClient(app)

@app.get("/")
def hello_world():
    return "FastAPI World!!"

def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.stauts_code != 500
    assert response.json() == "FastAPI World!!"

    