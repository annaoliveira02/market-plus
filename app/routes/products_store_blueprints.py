from flask import Blueprint
from app.controllers.products_users_controllers import (
    add_to_favorites,
    remove_from_favorites,
)

bp_products_store = Blueprint("bp_products_store", __name__)

bp_products_store.post("/favorites/<id>")(add_to_favorites)
bp_products_store.delete("/favorites/<id>")(remove_from_favorites)
