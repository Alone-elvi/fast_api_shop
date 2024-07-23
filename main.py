from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db

from schemas.user import UserCreate, UserUpdate
from schemas.category import CategoryCreate
from schemas.product import ProductCreate
from schemas.shop import ShopCreate

from crud.user import create_user, update_user
from crud.category import create_category
from crud.product import create_product
from crud.shop import create_shop



from routers import users, shops, products, categories, main, orders


app = FastAPI()


app.include_router(users.router)
app.include_router(shops.router)
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(orders.router)
app.include_router(main.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
    print("RabbitMQ order processor started")

