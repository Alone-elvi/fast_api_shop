from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# from models.product import Product
# from models.shop import Shop 

Base = declarative_base()

# Определение типов пользователей
USER_TYPES = {
    "customer": "Покупатель",
    "seller": "Продавец",
    "admin": "Администратор"
}

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone = Column(String)
    status = Column(String, default="active")
    created_at = Column(DateTime, default=datetime.now())
    favorite_product_id = Column(Integer, ForeignKey('products.id', ondelete='SET NULL'))
    user_type = Column(String, default="customer")

    favorite_product = relationship("Product", back_populates="favorited_by", foreign_keys=[favorite_product_id])
    shops = relationship("Shop", back_populates="owner", cascade="all, delete")
    orders = relationship("Order", back_populates="user", cascade="all, delete", foreign_keys='Order.user_id')