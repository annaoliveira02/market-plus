from flask import Blueprint
from app.controllers.store_img_controllers import show_store_image, upload_store_image

bp_store_img = Blueprint("bp_store_img", __name__)

bp_store_img.post('/images/stores')(upload_store_image)
bp_store_img.get('/images/stores/<id>')(show_store_image)