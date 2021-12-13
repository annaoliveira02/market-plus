from flask.helpers import send_file
from app.configs.database import db
from flask import request
from werkzeug.utils import secure_filename
from app.models.img_models import UserImage
from flask_jwt_extended import jwt_required, get_jwt_identity
from io import BytesIO

@jwt_required()
def upload():
    pic = request.files['pic']
    current = get_jwt_identity()

    if not pic:
        return {'alerta':'Nenhuma imagem enviada!'}, 400
    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return {'alerta':'Imagem inválida!'}, 400
    img = UserImage(img=pic.read(), name=filename, mimetype=mimetype, user_id=current["id"])
    db.session.add(img)
    db.session.commit()
    return {'alerta':'Imagem enviada!'}, 200

def show_photo(id):

    filé = UserImage.query.filter_by(user_id=id).first()
    return send_file(BytesIO(filé.img),attachment_filename=filé.name , as_attachment=False)