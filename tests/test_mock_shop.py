import pytest
from unittest.mock import patch, MagicMock, ANY
from sqlalchemy.orm import Session
from models import Shop
from crud.shop import get_shop
from schemas.shop import ShopResponse


@pytest.fixture
def mock_db_session():
    return MagicMock(spec=Session)


@pytest.fixture(scope="function")
def mock_get_shop():
    with patch("routers.shops.get_shop") as mock:
        yield mock


@pytest.fixture(scope="function")
def mock_get_db():
    with patch("routers.shops.get_db") as mock:
        yield mock


@pytest.fixture(scope="function")
def mock_read_shop():
    with patch("routers.shops.get_shop") as mock:
        yield mock


def test_get_shop_found(mock_db_session):
    mock_shop = MagicMock(spec=Shop)
    mock_shop.id = 1
    mock_shop.name = "Mock Shop"
    mock_shop.owner_id = 1

    mock_query = mock_db_session.query.return_value
    mock_filter = mock_query.filter.return_value
    mock_filter.first.return_value = mock_shop

    result = get_shop(mock_db_session, 1)

    assert result == mock_shop

    mock_db_session.query.assert_called_once_with(Shop)
    mock_query.filter.assert_called_once_with(ANY)
    mock_filter.first.assert_called_once_with()


def test_get_shop_not_found(mock_db_session):
    mock_query = mock_db_session.query.return_value
    mock_filter = mock_query.filter.return_value
    mock_filter.first.return_value = None

    result = get_shop(mock_db_session, 1)

    assert result is None

    mock_db_session.query.assert_called_once_with(Shop)
    mock_query.filter.assert_called_once_with(ANY)
    mock_filter.first.assert_called_once()

def test_read_shop(client, mock_read_shop):

    mock_shop = ShopResponse(id=1, name="Mock Shop", owner_id=1)
    mock_read_shop.return_value = mock_shop

    # Выполнение тестового запроса
    response = client.get("/shops/1")

    # Проверка ответа
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Mock Shop", "owner_id": 1}


class Any:
    def __eq__(self, other):
        return True
