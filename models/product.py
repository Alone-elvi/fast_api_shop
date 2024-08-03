from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from .user import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float, default=0.0)
    shop_id = Column(Integer, ForeignKey("shops.id", ondelete="CASCADE"))
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"))

    shop = relationship("Shop", back_populates="products")
    category = relationship("Category", back_populates="products")
    favorited_by = relationship(
        "User",
        back_populates="favorite_product",
        foreign_keys="User.favorite_product_id",
    )
