from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Integer
from app.exceptions.exceptions import NotAcessibleError, StoreAlreadyExistsError, StoreInvalidKeys
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates


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

    @staticmethod
    def validate_keys(data):
        allowed_keys = ["name", "address", "store_img", "phone_number", "cnpj", "password"]
        for key in data:
            if key not in allowed_keys:
                raise StoreInvalidKeys

    @validates("name", "adress", "store_img", "phone_number", "cnpj")
    def validates(self, key, value):
        if key == "name":
            unique_key = Stores.query.filter(Stores.name==value).first()
            if unique_key is not None:
                raise StoreAlreadyExistsError
        return value