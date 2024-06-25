from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .user import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

    products = relationship("Product", back_populates="category", cascade="all, delete")
    
