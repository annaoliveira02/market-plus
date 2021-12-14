from flask import Blueprint
from app.controllers.products_img_controller import upload_product, show_product_img

bp_product_img = Blueprint("bp_product_img", __name__)

bp_product_img.post('/images/products/<id>')(upload_product)
bp_product_img.get('/images/products/<id>')(show_product_img)