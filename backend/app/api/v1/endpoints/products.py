from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.db.session import get_db
from app.schemas.product import ProductInDB, ProductCreate
from app.services.product_service import get_product_service, ProductService

router = APIRouter()

@router.get("/", response_model=List[ProductInDB])
async def read_products(
    service: ProductService = Depends(get_product_service)
):
    """Retrieve all available products."""
    products = await service.get_all()
    return products

@router.post("/", response_model=ProductInDB, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    service: ProductService = Depends(get_product_service)
):
    """Create a new product."""
    product = await service.create(product_in)
    return product

@router.get("/{product_id}", response_model=ProductInDB)
async def read_product_by_id(
    product_id: int,
    service: ProductService = Depends(get_product_service)
):
    """Retrieve a specific product by its ID."""
    product = await service.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
