from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: int
    currency: str
    info: str
    short_description: str
    full_description: str
    

class Product(ProductBase):
    slug: str
    class Config:
        orm_mode = True

