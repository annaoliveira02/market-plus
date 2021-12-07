from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Integer, Float, Binary, DateTime

@dataclass
class Products(db.Model):
    id: int
    name: str
    category: str
    product_img: str
    price: str
    expiration_date: str

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    category = Column(String(30), nullable=False)
    product_img = Column(Binary)
    price = Column(Float, nullable=False)
    expiration_date = Column(DateTime, nullable=False)


