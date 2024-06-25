from sqlalchemy.orm import relationship

from .user import User
from .shop import Shop
from .product import Product
from .category import Category
from .order import Order

# Определение отношений после всех классов
User.favorite_product = relationship("Product", back_populates="favorited_by", foreign_keys=[User.favorite_product_id])
User.shops = relationship("Shop", back_populates="owner", cascade="all, delete")
User.orders = relationship("Order", back_populates="user", cascade="all, delete", foreign_keys='Order.user_id')

Shop.owner = relationship("User", back_populates="shops")
Shop.products = relationship("Product", back_populates="shop", cascade="all, delete")

Product.shop = relationship("Shop", back_populates="products")
Product.category = relationship("Category", back_populates="products")
Product.favorited_by = relationship("User", back_populates="favorite_product", foreign_keys="User.favorite_product_id")

Category.products = relationship("Product", back_populates="category", cascade="all, delete")

Order.user = relationship("User", back_populates="orders")
Order.product = relationship("Product")
