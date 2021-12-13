from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, String, Integer
from app.exceptions.exceptions import (
    InvalidKeyError,
    InvalidTypeError,
    NotAcessibleError,
    StoreAlreadyExistsError,
    StoreInvalidKeys,
)
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import backref, relationship, validates


@dataclass
class Stores(db.Model):
    id: int
    name: str
    address: str
    city: str
    state: str
    phone_number: str
    cnpj: str

    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(20), nullable=False)
    phone_number = Column(String(20))
    cnpj = Column(String(14), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)

    products = relationship(
        "Products", secondary="products_store", backref=backref("stores")
    )

    @property
    def password(self):
        raise NotAcessibleError("Password is not accessible")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def validate_password(self, input_password):
        return check_password_hash(self.password_hash, input_password)


    @validates("cnpj")
    def validates(self, key, cnpj):
        unique_key = Stores.query.filter(Stores.cnpj == cnpj).first()
        if unique_key is not None:
            raise StoreAlreadyExistsError
        return cnpj

    @staticmethod
    def validate_store_args(data):
        requested_args = ["name", "address", "city", "state", "phone_number", "cnpj", "password"]

        for item in requested_args:
            if item not in data.keys():
                raise InvalidKeyError

        for item in data.values():
            if type(item) is not str:
                raise InvalidTypeError

        for item in data.keys():
            if item not in requested_args:
                raise InvalidKeyError

    @staticmethod
    def validate_login_store(data):
        requested_args = ["cnpj", "password"]

        for item in requested_args:
            if item not in data.keys():
                raise InvalidKeyError

        for item in data.values():
            if type(item) is not str:
                raise InvalidTypeError

        for item in data.keys():
            if item not in requested_args:
                raise InvalidKeyError