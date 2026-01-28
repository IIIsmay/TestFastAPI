from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_chat():
    response = client.post(
        "/chats/",
        json={"title": "Test chat"}
    )

    assert response.status_code == 201 or response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["title"] == "Test chat"
    assert "created_at" in data
