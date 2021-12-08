from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, ForeignKey


@dataclass
class ProductsUserModel(db.Model):
    id: int
    product_id: int
    users_id: int

    __tablename__ = "products_users"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    users_id = Column(Integer, ForeignKey("users.id"), nullable=False)
