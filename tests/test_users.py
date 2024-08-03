import pytest

from conftest import client


def test_create_user(client):
    user = {
        "username": "Test User",
        "email": "9w9pY@example.com",
        "password": "testpassword",
        "user_type": "customer",
    }

    response = client.post("/users/", json=user)
    assert response.status_code == 200
    assert response.json() == {
        "username": "Test User",
        "email": "9w9pY@example.com",
        "password": response.json()["password"],
        "user_type": "customer",
    }


def test_update_user(client):
    user = {
        "username": "Test User",
        "email": "9w9pY@example.com",
        "user_type": "customer",
        "status": "active",
    }

    response = client.patch("/users/1", json=user)
    assert response.status_code == 200
    assert response.json() == {
        "username": "Test User",
        "email": "9w9pY@example.com",
        "user_type": "customer",
        "password": response.json()["password"],
        "status": "active",
    }
