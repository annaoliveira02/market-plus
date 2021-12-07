from dataclasses import dataclass
from sqlalchemy.sql.sqltypes import LargeBinary
from app.configs.database import db
from sqlalchemy import Column, String, Integer, Float, DateTime

@dataclass
class Products(db.Model):
    id: int
    name: str
    category: str
    product_img: str
    price: float

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    category = Column(String(30), nullable=False)
    product_img = Column(String)
    price = Column(Float, nullable=False)


