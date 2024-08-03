import pytest
from conftest import client


def test_create_product(client):
    product = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 10,
        "shop_id": 1,
        "category_id": 1,
    }
    response = client.post("/products/", json=product)
    assert response.status_code == 200
    assert response.json() == {
        "name": "Test Product",
        "description": "Test Description",
        "price": 10,
        "shop_id": 1,
        "category_id": 1,
    }


def test_get_products(client):
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "Test Product",
            "description": "Test Description",
            "price": 10,
            "shop_id": 1,
            "category_id": 1,
        }
    ]


def delete_product(client):
    response = client.delete("/products/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Product deleted"}
