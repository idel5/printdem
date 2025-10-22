from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    title: str
    price: float
    description: Optional[str] = None
    mockup_url: Optional[str] = None
    variants: List[str]

class ProductCreate(ProductBase):
    pass

class ProductInDB(ProductBase):
    id: int
    
    class Config:
        from_attributes = True
