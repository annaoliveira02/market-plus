from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Integer, Binary

@dataclass
class Stores(db.Model):
    id: int
    name: str
    city: str
    state: str
    country: str
    email: str
    password: str

    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    adress = Column(String(100), nullable=False)
    store_img = Column(Binary)
    phone_number = Column(String(20))

