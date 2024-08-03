from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int
    shop_id: int
    category_id: int

    class Config:
        from_attributes = True

    def __init__(self, **data):
        super().__init__(**data)
        self.from_attributes = True

    def __repr__(self):
        return f"Product(id={self.id!r}, name={self.name!r}, description={self.description!r}, price={self.price!r}, shop_id={self.shop_id!r}, category_id={self.category_id!r})"

    def __str__(self):
        return f"Product(id={self.id!r}, name={self.name!r}, description={self.description!r}, price={self.price!r}, shop_id={self.shop_id!r}, category_id={self.category_id!r})"


class ProductCreate(BaseModel):
    name: str
    description: str
    price: int
    shop_id: int
    category_id: int


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    shop_id: Optional[int] = None
    category_id: Optional[int] = None


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    shop_id: int
    category_id: int

    class Config:
        from_attributes = True

    def __init__(self, **data):
        super().__init__(**data)
        self.from_attributes = True

    def __repr__(self):
        return f"Product(id={self.id!r}, name={self.name!r}, description={self.description!r}, price={self.price!r}, shop_id={self.shop_id!r}, category_id={self.category_id!r})"

    def __str__(self):
        return f"Product(id={self.id!r}, name={self.name!r}, description={self.description!r}, price={self.price!r}, shop_id={self.shop_id!r}, category_id={self.category_id!r})"
    



class ProductList(BaseModel):
    products: list[ProductResponse] = []
