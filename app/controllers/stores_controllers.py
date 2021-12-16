from flask import request, current_app, jsonify
from flask_jwt_extended.utils import create_access_token
from app.exceptions.exceptions import (
    InvalidKeyError,
    InvalidTypeError,
    NotFoundError,
    StoreAlreadyExistsError
)
from app.models.stores_models import Stores
from flask_jwt_extended import jwt_required


def register_store():
    try:
        data = request.get_json()
        Stores.validate_store_args(data)
        stores = Stores(**data)
        current_app.db.session.add(stores)
        current_app.db.session.commit()
        return jsonify(stores), 201
    except StoreAlreadyExistsError as e:
        return e.message, 409
    except InvalidKeyError:
        return {
            "alerta": "Informações incorretas (nome, endereço, cidade, estado, número, cnpj e senha)."
        }, 400
    except InvalidTypeError:
        return {"alerta": "Informações inválidas (apenas texto)."}, 400


def get_all():
    result = Stores.query.all()
    if len(result) == 0:
        return {"alerta": "Nenhum dado encontrado"}, 404
    return (
        jsonify(
            [
                {
                    "id": store.id,
                    "name": store.name,
                    "address": store.address,
                    "city": store.city,
                    "state": store.state,
                    "phone_number": store.phone_number,
                    "cnpj": store.cnpj,
                    "products": [
                        {
                            "name": product.name,
                            "category": product.category,
                            "price": product.price
                        }
                        for product in store.products
                    ],
                }
                for store in result
            ]
        ),
        200,
    )


@jwt_required()
def delete_stores(id):
    current = Stores.query.get(id)
    if current is None:
        return {"alerta": "Loja não encontrada"}, 404
    current_app.db.session.delete(current)
    current_app.db.session.commit()
    return "", 204


def get_stores_id(id):
    current = Stores.query.get(id)
    if current is None:
        return {"alerta": "Loja não encontrada"}, 404
    return (
        jsonify(
            [
                {
                    "id": store.id,
                    "name": store.name,
                    "address": store.address,
                    "city": store.city,
                    "state": store.state,
                    "phone_number": store.phone_number,
                    "cnpj": store.cnpj,
                    "products": [
                        {
                            "name": product.name,
                            "category": product.category,
                            "price": product.price
                        }
                        for product in store.products
                    ],
                }
                for store in current
            ]
        ),
        200,
    )



def login_store():
    try:
        data = request.json
        Stores.validate_login_store(data)
        store = Stores.query.filter_by(cnpj=data["cnpj"]).first()
        if not store:
            raise NotFoundError
        if store.validate_password(data["password"]):
            token = create_access_token(store)
            return {"token": token}, 200
    except InvalidKeyError:
        return {"alerta": "Apenas cnpj e senha"}, 401
    except InvalidTypeError:
        return {"alerta": "Informações inválidas (apenas texto)."}, 400
    except NotFoundError:
        return {"alerta": "Cadastro não encontrado"}, 404


def get_page():
    list = Stores.query.all()
    if request.args != {}:
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
        start = (page - 1) * per_page
        end = page * per_page
        limited_list = list[start:end]
    if request.args == {}:
        limited_list = list[0:10]
    return (
        jsonify(
            [
                {
                    "id": store.id,
                    "name": store.name,
                    "address": store.address,
                    "city": store.city,
                    "state": store.state,
                    "phone_number": store.phone_number,
                    "cnpj": store.cnpj,
                    "products": [
                        {
                            "name": product.name,
                            "category": product.category,
                        }
                        for product in store.products
                    ],
                }
                for store in limited_list
            ]
        ),
        200,
    )

def get_city():
    keys = request.args.keys()
    city = str(request.args.get('city'))
    name = str(request.args.get('name'))
    if request.args == {}:
        list = Stores.query.all()
    if "city" in keys:
        list = Stores.query.filter(Stores.city==city).all()
    if "name" in keys:
        list = Stores.query.filter(Stores.name== name).all()
    return (
        jsonify(
            [
                {
                    "id": store.id,
                    "name": store.name,
                    "address": store.address,
                    "city": store.city,
                    "state": store.state,
                    "phone_number": store.phone_number,
                    "cnpj": store.cnpj,
                    "products": [
                        {
                            "name": product.name,
                            "category": product.category,
                        }
                        for product in store.products
                    ],
                }
                for store in list
            ]
        ),
        200,
    )


