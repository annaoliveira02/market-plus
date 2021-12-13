from sqlalchemy import Column, Text, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import LargeBinary
from app.configs.database import db


class ProductImg(db.Model):

    __tablename__ = "products_img"

    id = Column(Integer, primary_key=True)
    img = Column(LargeBinary, nullable=False)
    name = Column(Text, nullable=False)
    mimetype = Column(Text, nullable=False)
    products_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    
