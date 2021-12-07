from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Integer

@dataclass
class Users(db.Model):
    id: int
    name: str
    city: str
    state: str
    country: str
    email: str
    password: str

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    city = Column(String(100), nullable=False)
    state = Column(String(2), nullable=False)
    country = Column(String(6), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    state = Column(String(20), nullable=False)

