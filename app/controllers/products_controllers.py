from flask import request, current_app, jsonify, json
from app.exceptions.exceptions import (
    InvalidKeyError,
    NotFoundError,
    ProductAlreadyExistsError,
)

from app.models.products_models import Products
from flask_jwt_extended import jwt_required


@jwt_required()
def register_products():
    try:
        data = request.get_json()
        products = Products(**data)
        current_app.db.session.add(products)
        current_app.db.session.commit()
        return jsonify(products)
    except ProductAlreadyExistsError as e:
        return e.message
    except TypeError:
        return {
            "error": "Chave inválida! Só são permitidas as chaves: `name`, `category`, `procut_img` e `price`."
        }


def get_all():
    result = Products.query.all()
    try:
        Products.validate_id(result)
    except NotFoundError as e:
        return e.message, 404
    return jsonify(result), 200

@jwt_required()
def change_products(id):
    product = Products.query.filter(Products.id==id).one_or_none()
    try:
        current= Products.query.get(id)
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
        "price": product.price
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
