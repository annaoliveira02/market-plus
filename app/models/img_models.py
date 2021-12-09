from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db


class Img(db.Model):
    id = Column(db.Integer, primary_key=True)
    img = Column(db.Text, unique=True, nullable=False)
    name = Column(db.Text, nullable=False)
    mimetype = Column(db.Text, nullable=False)
