from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, ForeignKey, Float

from app.exceptions.exceptions import InvalidKeyError, InvalidTypeError


@dataclass
class ProductsStoreModel(db.Model):
    id: int
    product_id: int
    store_id: int
    price_by_store: float

    __tablename__ = "products_store"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)
    price_by_store = Column(Float)

    @staticmethod
    def validate_patch_args(data):
        if 'price' not in data.keys() or len(data.keys()) > 1:
            raise InvalidKeyError

        if type(data["price"]) is not float:
            raise InvalidTypeError
