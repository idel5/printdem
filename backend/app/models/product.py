from sqlalchemy import Column, String, Float, ARRAY, Integer # <-- ADDED INTEGER
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Product(Base):
    __tablename__ = "product"
    

    id = Column(Integer, primary_key=True, index=True) 

    title = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    mockup_url = Column(String, nullable=True)
    variants = Column(ARRAY(String), nullable=False)
