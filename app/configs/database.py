from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)

    app.db = db

    from app.models.stores_models import Stores
    from app.models.user_models import Users
    from app.models.products_models import Products
    from app.models.sugestion_models import Sugestions
    from app.models.products_user_models import ProductsUserModel
    from app.models.products_store_models import ProductsStoreModel
    from app.models.img_models import UserImage
    from app.models.products_img_models import ProductImg
    from app.models.store_img_models import StoreImage