from flask import Blueprint
from app.controllers.img_controllers import upload

bp_img = Blueprint("bp_img", __name__)

bp_img.post('/images')(upload)