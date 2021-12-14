from sqlalchemy import Column, Text, Integer, Float
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import LargeBinary
from app.configs.database import db


class StoreImage(db.Model):

    __tablename__ = "stores_img"

    id = Column(Integer, primary_key=True)
    img = Column(LargeBinary, nullable=False)
    name = Column(Text, nullable=False)
    mimetype = Column(Text, nullable=False)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)
    
