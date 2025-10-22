from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional

from app.models.product import Product
from app.schemas.product import ProductCreate
from app.db.session import get_db


class ProductService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[Product]:
        result = await self.db.execute(select(Product))
        return result.scalars().all()

    async def get_by_id(self, product_id: int) -> Optional[Product]:
        result = await self.db.execute(
            select(Product).where(Product.id == product_id)
        )
        return result.scalar_one_or_none()

    async def create(self, product_in: ProductCreate) -> Product:
        db_product = Product(**product_in.model_dump())
        self.db.add(db_product)
        await self.db.commit()
        await self.db.refresh(db_product)
        return db_product

async def get_product_service(db: AsyncSession= Depends(get_db)) -> ProductService:
    return ProductService(db)
