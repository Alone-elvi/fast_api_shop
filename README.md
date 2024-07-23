```markdown
# Order Processing Module

## Описание

Модуль обработки заказов предназначен для управления заказами в системе. Он включает в себя серверное приложение на основе FastAPI, базу данных PostgreSQL для хранения данных и RabbitMQ для асинхронной обработки сообщений.

## Установка и настройка

### Требования

- Docker
- Docker Compose

### Шаги установки

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/your-repo/order-processing-module.git
    cd order-processing-module
    ```

2. Создайте файл `Dockerfile` в корне проекта:

    ```Dockerfile
    # Используем официальный образ Python
    FROM python:3.12-slim

    # Устанавливаем зависимости
    RUN apt-get update && apt-get install -y \
        build-essential \
        libpq-dev \
        && rm -rf /var/lib/apt/lists/*

    # Устанавливаем рабочую директорию
    WORKDIR /app

    # Копируем файлы проекта
    COPY . /app

    # Устанавливаем Python-зависимости
    RUN pip install --upgrade pip
    RUN pip install -r requirements.txt

    # Открываем порт для приложения
    EXPOSE 8000

    # Команда для запуска приложения
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    ```

3. Создайте файл `docker-compose.yml` в корне проекта:

    ```yaml
    version: '3.9'

    services:
      db:
        image: postgres
        restart: always
        environment:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: postgres
        ports:
          - "5432:5432"

      rabbitmq:
        image: rabbitmq:3-management
        restart: always
        ports:
          - "5672:5672"
          - "15672:15672"

      web:
        build: .
        command: ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
        volumes:
          - .:/app
        ports:
          - "8000:8000"
        depends_on:
          - db
          - rabbitmq
        environment:
          DATABASE_URL: "postgresql://postgres@db:5432/postgres"
          RABBITMQ_URL: "amqp://guest:guest@rabbitmq:5672/"
    ```

4. Создайте файл `requirements.txt` в корне проекта:

    ```plaintext
    fastapi
    uvicorn
    sqlalchemy
    psycopg2-binary
    pydantic
    pytest
    alembic
    pika
    ```

## Использование

### Запуск контейнеров

Чтобы запустить контейнеры, выполните следующую команду:

```sh
docker-compose up --build
```

### Примеры API запросов

- Создание заказа:

    ```sh
    curl -X POST "http://localhost:8000/orders/" -H "Content-Type: application/json" -d '{"user_id": 1, "product_id": 1, "quantity": 3}'
    ```

- Обновление магазина:

    ```sh
    curl -X PUT "http://localhost:8000/shops/1" -H "Content-Type: application/json" -d '{"name": "New Shop Name", "owner_id": 2}'
    ```

## Тестирование

Для запуска тестов используйте `pytest`. Убедитесь, что вы находитесь в виртуальном окружении с установленными зависимостями, и выполните следующую команду:

```sh
pytest -v
```
