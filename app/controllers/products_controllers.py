from flask import request, current_app, jsonify, json
from app.exceptions.exceptions import (
    InvalidKeyError,
    NotFoundError,
    ProductAlreadyExistsError,
)

from app.models.products_models import Products


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


def change_products():
    data = request.json
    product = Products.query.filter(Products.id == data["id"]).first()
    try:
        Products.validate_id(product)
    except NotFoundError as e:
        return e.message, 404

    for key, value in data.items():
        setattr(product, key, value)

    current_app.db.session.add(product)
    current_app.db.session.commit()

    return "", 204


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
