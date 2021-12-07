from dataclasses import dataclass
from sqlalchemy.sql.sqltypes import LargeBinary
from app.configs.database import db
from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.orm import validates
import psycopg2

from app.exceptions.exceptions import (
    InvalidKeyError,
    NotFoundError,
    ProductAlreadyExistsError,
)


@dataclass
class Products(db.Model):
    allowed_keys = ["name", "category", "product_img", "price"]
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

    @validates("name", "category", "product_img", "price")
    def validates(self, key, value):
        if key == "name":
            unique_key = Products.query.filter(Products.name == value).one_or_none()
            if unique_key is not None:
                raise ProductAlreadyExistsError
        return value

    def validate_id(current):
        if current is None:
            raise NotFoundError
        if type(current) != Products and len(current) == 0:
            raise NotFoundError
