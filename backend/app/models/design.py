from sqlalchemy import Column, String, Text, Integer
from app.db.base_class import Base

class Design(Base):

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=False)
    file_url = Column(String, nullable=False)
    name = Column(String, nullable=False)
    fabric_json = Column(Text, nullable=True)
