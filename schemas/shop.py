from pydantic import BaseModel
from typing import Optional


class ShopCreate(BaseModel):
    name: str
    owner_id: int


class ShopUpdate(BaseModel):
    name: Optional[str] = None
    owner_id: Optional[int] = None


class ShopResponse(BaseModel):
    id: int
    name: str
    owner_id: int

    class Config:
        orm_mode = True
