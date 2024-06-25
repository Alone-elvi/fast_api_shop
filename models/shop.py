from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .user import User, Base

class Shop(Base):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))

    owner = relationship("User", back_populates="shops")
    products = relationship("Product", back_populates="shop", cascade="all, delete")

User.shops = relationship("Shop", back_populates="owner")
