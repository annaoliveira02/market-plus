from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Integer, ForeignKey

from app.exceptions.exceptions import InvalidKeyError, InvalidTypeError

@dataclass
class Sugestions(db.Model):
    id: int
    type: str
    message: str
    users_id: int

    __tablename__ = "sugestions"

    id = Column(Integer, primary_key=True)
    type = Column(String(20), nullable=False)
    message = Column(String(250), nullable=False)
    users_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    @staticmethod
    def validate_post_args(data):
        requested_args = ["type", "message"]

        for item in requested_args:
            if item not in data.keys():
                raise InvalidKeyError
        
        for item in data.values():
            if type(item) is not str:
                raise InvalidTypeError
            
        for item in data.keys():
            if item not in requested_args:
                raise InvalidKeyError