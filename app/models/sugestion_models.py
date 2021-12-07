from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Integer, ForeignKey

@dataclass
class Users(db.Model):
    id: int
    type: str
    message: str
    users_id: int

    __tablename__ = "sugestions"

    id = Column(Integer, primary_key=True)
    type = Column(String(20), nullable=False)
    message = Column(String(250), nullable=False)
    users_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    