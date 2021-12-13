from flask.helpers import send_file
from app.configs.database import db
from flask import request
from werkzeug.utils import secure_filename
from app.models.products_img_models import ProductImg
from flask_jwt_extended import jwt_required, get_jwt_identity
from io import BytesIO

@jwt_required()
def upload_product(id):
    product = request.files['product']
    current = get_jwt_identity()
    if 'cnpj' not in current:
        return {'alerta':'Usuário não autorizado para cadastrar imagem'}, 401
    print(current)
    if not product:
        return {'alerta':'Nenhuma imagem de produto enviada!'}, 400
    filename = secure_filename(product.filename)
    mimetype = product.mimetype
    if not filename or not mimetype:
        return {'alerta':'Imagem inválida!'}, 400
    img = ProductImg(img=product.read(), name=filename, mimetype=mimetype, products_id=id)
    db.session.add(img)
    db.session.commit()
    return {'alerta':'Imagem enviada!'}, 200

def show_product_img(id):

    file = ProductImg.query.filter_by(products_id=id).first()
    return send_file(BytesIO(file.img), attachment_filename=file.name , as_attachment=False)