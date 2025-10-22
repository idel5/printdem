from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, DateTime, func
import re

class CustomBase:
    @declared_attr
    def __tablename__(cls):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    id = Column(
        'id',
        autoincrement=True,
        primary_key=True
    )
    
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

Base = declarative_base(cls=CustomBase)
