# tests/test_categories.py
import pytest
from conftest import client


def test_create_category(client):
    category = {"name": "Test Category"}
    response = client.post("/categories/", json=category)
    assert response.status_code == 200
    assert response.json() == {"name": "Test Category"}


def test_get_categories(client):
    response = client.get("/categories/")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Test Category"}]


def test_update_category(client):
    category = {"name": "Updated Category"}
    try:
        response = client.patch("/categories/1", json=category)
        if response.status_code == 200:
            assert response.json() == {"id": 1, "name": "Updated Category"}
        else:
            assert False
    except Exception as e:
        assert str(e) == "Not found"


def test_delete_category(client):
    response = client.delete("/categories/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Category deleted"}
