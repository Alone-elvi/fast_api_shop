import pytest


@pytest.mark.parametrize("shop_id", [1, 2, 3])
def test_create_shop(client, shop_id):
    shop = {"name": "Test Shop", "owner_id": shop_id}
    response = client.post(f"/shops/", json=shop)
    assert response.status_code == 200
    assert response.json() == {"id": shop_id, "name": "Test Shop", "owner_id": shop_id}


@pytest.mark.parametrize("shop_id", [1, 2, 3])
def test_get_shop(client, shop_id):
    response = client.get(f"/shops/{shop_id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": shop_id,
        "name": "Test Shop",
        "owner_id": shop_id,
    }


@pytest.mark.parametrize("shop_id", [1, 2, 3])
def test_update_shop(client, shop_id):
    shop = {"name": "Updated Shop", "owner_id": shop_id}
    response = client.patch(f"/shops/{shop_id}", json=shop)
    assert response.status_code == 200
    assert response.json() == {
        "id": shop_id,
        "name": "Updated Shop",
        "owner_id": shop_id,
    }


@pytest.mark.parametrize("shop_id", [5, 6, 7])
def test_get_shops_error_xfail(client, shop_id):
    if shop_id in [5, 6, 7]:
        pytest.xfail("This shop_id is expected to fail")
    response = client.get(f"/shops/{shop_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Shop not found"}


@pytest.mark.parametrize("shop_id", [1, 2, 3])
def test_delete_shop(client, shop_id):
    response = client.delete(f"/shops/{shop_id}")
    assert response.json() == {"message": "Shop deleted"}
