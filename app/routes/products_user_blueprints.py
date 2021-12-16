from flask import Blueprint
from app.controllers.products_users_controllers import (
    add_to_favorites,
    get_favorites,
    remove_from_favorites,
)

bp_favorites = Blueprint("bp_favorites", __name__)

bp_favorites.post("/favorites/<id>")(add_to_favorites)
bp_favorites.delete("/favorites/<id>")(remove_from_favorites)
bp_favorites.get("/favorites")(get_favorites)