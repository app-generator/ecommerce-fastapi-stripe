from fastapi import APIRouter, HTTPException, status
from typing import List

from src import schemas
from src.helpers.utils import get_local_products

router = APIRouter(
    prefix = "/api/products",
    tags = ['Products']
)

@router.get("/", response_model=List[schemas.Product])
async def get_products():
    
    products = get_local_products()

    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product Was Not Found')

    return products


@router.get("/{id}", response_model=schemas.Product)
async def get_product(id: int):

    products = get_local_products()

    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product was not found")
    
    try:
        product = products[id]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product was not found")

    return product