from flask import Blueprint
from app.controllers.products_controllers import (
    add_to_database,
    get_all,
    register_products,
    change_products,
    delete_products,
    get_by_id, get_category, add_to_store
)

bp_products = Blueprint("bp_products", __name__)

bp_products.get("/products")(get_all)
bp_products.post("/products")(add_to_database)
bp_products.get("/products/<id>")(get_by_id)
bp_products.patch("/products/<id>")(change_products)
bp_products.delete("/products/<id>")(delete_products)
bp_products.get("/products/list")(get_category)
bp_products.post("/products/<id>")(add_to_store)