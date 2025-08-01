from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI app!"}

def test_greet():
    response = client.get("/greet")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Developer 👋"}
