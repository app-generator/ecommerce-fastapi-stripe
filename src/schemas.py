from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    currency: str
    info: str
    short_description: str
    full_description: str
    

class Product(ProductBase):
    # id: int
    class Config:
        orm_mode = True

