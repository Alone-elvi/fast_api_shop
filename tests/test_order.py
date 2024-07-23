# tests/test_order.py

def test_create_order(client):
    order = {"user_id": 1, "product_id": 2, "quantity": 3}
    response = client.post("/orders/", json=order)
    assert response.status_code == 200
    assert response.json() == {"message": "Order received and is being processed"}

def test_process_order(db_session):
    # Пример теста, который взаимодействует с базой данных
    from models.order import Order
    new_order = Order(user_id=1, product_id=2, quantity=3)
    db_session.add(new_order)
    db_session.commit()
    db_session.refresh(new_order)
    assert new_order.id is not None


def test_delete_order(db_session):
    from models.order import Order

    # Создание и добавление заказа в базу данных
    deleted_order = Order(user_id=1, product_id=2, quantity=3)
    db_session.add(deleted_order)
    db_session.commit()
    db_session.refresh(deleted_order)
    
    # Убедитесь, что заказ был успешно создан и имеет идентификатор
    assert deleted_order.id is not None

    # Удаление заказа из базы данных
    db_session.delete(deleted_order)
    db_session.commit()

    # Попытка обновления удаленного объекта вызовет ошибку, поэтому это не делаем
    # Вместо этого, проверяем, что объект действительно удален с помощью запроса к базе данных
    deleted_order_from_db = db_session.query(Order).filter(Order.id == deleted_order.id).first()
    assert deleted_order_from_db is None


def test_update_shop(client):
    # Создание магазина для теста
    response = client.post("/shops/", json={"name": "Old Shop Name", "owner_id": 2})
    assert response.status_code == 200
    print(response.json())
    shop_id = response.json()["id"]


    # Обновление магазина
    update_data = {"name": "New Shop Name", "owner_id": 2}
    response = client.put(f"/shops/{shop_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "New Shop Name"
    assert response.json()["owner_id"] == 2
