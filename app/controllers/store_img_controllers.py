from flask.helpers import send_file
from app.configs.database import db
from flask import request
from werkzeug.utils import secure_filename
from app.models.store_img_models import StoreImage
from flask_jwt_extended import jwt_required, get_jwt_identity
from io import BytesIO

@jwt_required()
def upload_store_image():
    img = request.files['img']
    current = get_jwt_identity()

    if not img:
        return {'alerta':'Nenhuma imagem enviada!'}, 400
    filename = secure_filename(img.filename)
    mimetype = img.mimetype
    if not filename or not mimetype:
        return {'alerta':'Imagem inválida!'}, 400
    photo = StoreImage(img=img.read(), name=filename, mimetype=mimetype, store_id=current["id"])
    db.session.add(photo)
    db.session.commit()
    return {'alerta':'Imagem enviada!'}, 200

def show_store_image(id):

    file = StoreImage.query.filter_by(store_id=id).first()
    return send_file(BytesIO(file.img),attachment_filename=file.name , as_attachment=False)