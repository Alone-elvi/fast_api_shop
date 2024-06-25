from pydantic import BaseModel


class ShopCreate(BaseModel):
    name: str
    owner_id: int
