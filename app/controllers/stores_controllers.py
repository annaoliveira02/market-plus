from flask import request, current_app, jsonify
from flask_jwt_extended.utils import create_access_token
from app.exceptions.exceptions import InvalidKeyError, StoreAlreadyExistsError, StoreInvalidKeys
from app.models.stores_models import Stores
from flask_jwt_extended import jwt_required

def register_store():
    try:
        data = request.get_json()
        Stores.validate_keys(data)   
        stores = Stores(**data)
        current_app.db.session.add(stores)
        current_app.db.session.commit()
        return jsonify(stores), 201
    except StoreAlreadyExistsError as e:
        return e.message, 409
    except StoreInvalidKeys as e:
        return e.message, 400

def get_all():
    result= Stores.query.all()
    if len(result) == 0:
        return {"msg": "Nenhum dado encontrado"}, 404
    return jsonify(result), 200

@jwt_required()
def delete_stores(id):
    current= Stores.query.get(id)
    if current== None: 
        return{"message": "Loja não encontrada"},404
    current_app.db.session.delete(current)
    current_app.db.session.commit()
    return "", 204  

def get_stores_id(id):
    current= Stores.query.get(id)
    if current== None: 
        return{"message": "Loja não encontrada"},404
    return jsonify(current) 

def login_store():
    try:
        data = request.json
        store = Stores.query.filter_by(cnpj=data["cnpj"]).first()
        if not store:
            raise InvalidKeyError
        if store.validate_password(data['password']):
            token = create_access_token(store)
            return {"token": token}, 200
    except InvalidKeyError:
        return {"msg": "CNPJ ou senha inválidos"}, 401