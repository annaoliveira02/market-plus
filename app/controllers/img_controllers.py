from app.configs.database import db
from flask import request
from werkzeug.utils import secure_filename
from app.models.img_models import Img
from flask_jwt_extended import jwt_required, get_jwt_identity

def upload():
    pic = request.files['pic']
    # pic["users_id"] = id

    if not pic:
        return 'No pic uploaded!', 400
    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400
    img = Img(img=pic.read(), name=filename, mimetype=mimetype)
    db.session.add(img)
    db.session.commit()
    return 'Img Uploaded!', 200