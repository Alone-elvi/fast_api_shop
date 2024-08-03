from pydantic import BaseModel


class CategoryShema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

    def __init__(self, **data):
        super().__init__(**data)
        self.from_attributes = True

    def __repr__(self):
        return f"Category(id={self.id!r}, name={self.name!r})"

    def __str__(self):
        return f"Category(id={self.id!r}, name={self.name!r})"


class CategoryCreate(BaseModel):
    name: str


class CategoriesResponse(BaseModel):
    categories: list[CategoryShema]

    class Config:
        from_attributes = True

    def __init__(self, **data):
        super().__init__(**data)
        self.from_attributes = True

    def __repr__(self):
        return f"CategoriesResponse(categories={self.categories!r})"

    def __str__(self):
        return f"CategoriesResponse(categories={self.categories!r})"
