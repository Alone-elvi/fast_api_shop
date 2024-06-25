from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from .user import Base
import datetime


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    quantity = Column(Integer)
    order_date = Column(DateTime, default=datetime.datetime.now())
    status = Column(String, default="processing")

    user = relationship("User", back_populates="orders")
    product = relationship("Product")
