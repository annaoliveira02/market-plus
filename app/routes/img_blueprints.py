from flask import Blueprint
from app.controllers.img_controllers import upload, show_photo

bp_img = Blueprint("bp_img", __name__)

bp_img.post('/images/users')(upload)
bp_img.get('/images/users/<id>')(show_photo)