from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str
    price: int
    shop_id: int
    category_id: int
