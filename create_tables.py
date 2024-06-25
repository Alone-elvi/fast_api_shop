from sqlalchemy import create_engine

from models.user import Base
from models.user import User
from models.shop import Shop
from models.product import Product
from models.category import Category
from db import engine


Base.metadata.create_all(bind=engine)