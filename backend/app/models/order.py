from sqlalchemy import Column, String, Float, Integer
from app.db.base_class import Base

class Order(Base):

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String, default="Pending", nullable=False)
