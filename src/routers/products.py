# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

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


@router.get("/{slug}", response_model=schemas.Product)
async def get_product_by_slug(slug: str):

    products = get_local_products()

    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product was not found")

    for product in products:
        if product['slug']==slug:
            return product

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product was not found")

