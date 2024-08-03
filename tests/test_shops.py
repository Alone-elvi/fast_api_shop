import pytest
from conftest import client


def test_create_shop(client):
    shop = {"name": "Test Shop", "owner_id": 1}
    response = client.post("/shops/", json=shop)
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Shop", "owner_id": 1}


def test_get_shop(client):
    response = client.get("/shops/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Test Shop",
        "owner_id": 1,
    }


def test_update_shop(client):
    shop = {"name": "Updated Shop", "owner_id": 1}
    response = client.patch("/shops/1", json=shop)
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Updated Shop",
        "owner_id": 1,
    }

def test_delete_shop(client):
    response = client.delete("/shops/1")
    assert response.json() == {"message": "Shop deleted"}
