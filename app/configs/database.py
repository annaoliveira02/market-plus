from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)

    app.db = db

    from app.models.sugestion_models import Sugestions
    from app.models.stores_models import Stores
    from app.models.products_models import Products
    from app.models.user_models import Users
   