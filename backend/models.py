from database import Base
from sqlalchemy import Column, Integer, String

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    uid = Column(String, nullable=False)
