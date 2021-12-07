from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Integer
from app.exceptions.exceptions import NotAcessibleError
from werkzeug.security import generate_password_hash, check_password_hash
 
@dataclass
class Users(db.Model):
    id: int
    name: str
    city: str
    state: str
    country: str
    email: str

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    city = Column(String(100), nullable=False)
    state = Column(String(2), nullable=False)
    country = Column(String(6), nullable=False, default="Brasil")
    email = Column(String(30), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)

    @property
    def password(self):
        raise NotAcessibleError('Password is not accessible')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def validate_password(self, input_password):
        return check_password_hash(self.password_hash, input_password)