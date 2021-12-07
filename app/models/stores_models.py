from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Integer
from app.exceptions.exceptions import NotAcessibleError
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class Stores(db.Model):
    id: int
    name: str
    address: str
    store_img: str
    phone_number: str
    cnpj: str

    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    store_img = Column(String)
    phone_number = Column(String(20))
    cnpj = Column(String(14), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)

    @property
    def password(self):
        raise NotAcessibleError('Password is not accessible')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def validate_password(self, input_password):
        return check_password_hash(self.password_hash, input_password)
