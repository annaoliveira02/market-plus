from flask import Blueprint
from app.controllers.products_controllers import (
    get_all,
    register_products,
    change_products,
    delete_products,
    get_by_id, get_category, patching_products_price
)

bp_products = Blueprint("bp_products", __name__)

bp_products.get("/products")(get_all)
bp_products.post("/products")(register_products)
bp_products.get("/products/<id>")(get_by_id)
bp_products.patch("/products/<id>")(change_products)
bp_products.delete("/products/<id>")(delete_products)
bp_products.get("/products/list")(get_category)
bp_products.patch("/products")(patching_products_price)