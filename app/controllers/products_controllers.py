from flask import request, current_app, jsonify
from flask_jwt_extended.utils import get_jwt_identity
from app.exceptions.exceptions import (
    InvalidKeyError,
    InvalidTypeError,
    NotFoundError,
    ProductAlreadyExistsError,
)
from app.models.products_models import Products
from flask_jwt_extended import jwt_required

from app.models.products_store_models import ProductsStoreModel


@jwt_required()
def register_products():
    try:
        data = request.get_json()
        current_store = get_jwt_identity()
        Products.validate_keys(data)
        product = Products(**data)
        current_app.db.session.add(product)
        current_app.db.session.commit()

        data2 = {
            "product_id": product.id,
            "store_id": current_store["id"],
            "price_by_store": product.price,
        }
        products_store = ProductsStoreModel(**data2)
    except ProductAlreadyExistsError as e:
        return e.message, 409
    except TypeError:
        return {
            "error": "Chave inválida! Deve conter somente as chaves: `name`, `category`, `procut_img` e `price`."
        }, 409
    except InvalidKeyError:
        return {
            "error": "Chave inválida! Deve conter somente as chaves: `name`, `category`, `procut_img` e `price`."
        }, 409
    except InvalidTypeError:
        return {
            "error": "`name`, `category`, `procut_img` devem ser do tipo `str` e `price` deve ser do tipo `float`"
        }, 409

    current_app.db.session.add(products_store)
    current_app.db.session.commit()
    return jsonify(product)


def get_all():
    result = Products.query.all()
    try:
        Products.validate_id(result)
    except NotFoundError as e:
        return e.message, 404
    return (
        jsonify(
            [
                {
                    "id": product.id,
                    "name": product.name,
                    "category": product.category,
                    "product_img": product.product_img,
                    "price": product.price,
                    "stores": [
                        {
                            "name": store.name,
                            "address": store.address,
                            "store_img": store.store_img,
                            "phone_number": store.phone_number,
                        }
                        for store in product.stores
                    ],
                }
                for product in result
            ]
        ),
        200,
    )


@jwt_required()
def change_products(id):
    product = Products.query.filter(Products.id == id).one_or_none()
    try:
        data = request.get_json()
        Products.validate_id(product)

        for key, value in data.items():
            setattr(product, key, value)

        current_app.db.session.add(product)
        current_app.db.session.commit()

        return {
            "id": product.id,
            "name": product.name,
            "category": product.category,
            "product_img": product.product_img,
            "price": product.price,
        }, 200
    except NotFoundError as e:
        return e.message, 404


@jwt_required()
def delete_products(id):
    current = Products.query.get(id)
    try:
        Products.validate_id(current)
    except NotFoundError as e:
        return e.message, 404
    current_app.db.session.delete(current)
    current_app.db.session.commit()
    return "", 204


def get_by_id(id):
    current = Products.query.get(id)
    try:
        Products.validate_id(current)
    except NotFoundError as e:
        return e.message, 404

    return jsonify(current)
