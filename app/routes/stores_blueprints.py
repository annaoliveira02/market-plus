from flask import Blueprint
from app.controllers.stores_controllers import (
    get_all,
    login_store,
    register_store,
    delete_stores,
    get_stores_id,
)


bp_stores = Blueprint("bp_stores", __name__)

bp_stores.get("/stores")(get_all)
bp_stores.post("/stores")(register_store)
bp_stores.post("/login_stores")(login_store)
bp_stores.get("/stores/<id>")(get_stores_id)
bp_stores.delete("/stores/<id>")(delete_stores)
