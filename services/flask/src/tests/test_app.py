from http.cookies import SimpleCookie
import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200


def test_login_actions(client):
    with client.session_transaction() as session:
        session["username"] = "user"
    response = client.post("/login", data={"username": "user"})
    assert response.status_code == 302

    cookie = SimpleCookie()
    cookie.load(response.headers["Set-Cookie"])
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    assert cookies.get("session")

    client.set_cookie("session", cookies["session"])
    response = client.post("/send_message", data={"message": "test"})
    assert response.status_code == 204

    response = client.get("fetch_chat")
    assert response.status_code == 200
    data_json = json.loads(response.text)
    assert len(data_json) == 1
    assert data_json[0]["content"] == "test"
    assert data_json[0]["user"] == "user"

# TODO: test event
