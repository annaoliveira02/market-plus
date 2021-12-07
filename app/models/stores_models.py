from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import LargeBinary
from app.configs.database import db
from sqlalchemy import Column, String, Integer

@dataclass
class Stores(db.Model):
    id: int
    name: str
    address: str
    store_img: str
    phone_number: str

    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    address = Column(String(100), nullable=False)
    store_img = Column(String)
    phone_number = Column(String(20))

