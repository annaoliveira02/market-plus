from sqlalchemy import Column, Text, Integer, Float
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import LargeBinary
from app.configs.database import db


class UserImage(db.Model):

    __tablename__ = "users_img"

    id = Column(Integer, primary_key=True)
    img = Column(LargeBinary, nullable=False)
    name = Column(Text, nullable=False)
    mimetype = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
