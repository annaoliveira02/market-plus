from flask import request, current_app, jsonify
from flask_jwt_extended.utils import get_jwt_identity
from app.exceptions.exceptions import (
    InvalidKeyError,
    InvalidTypeError,
    NotFoundError,
    ProductAlreadyExistsError,
)
from app.models.products_models import Products
from app.models.user_models import Users
from flask_jwt_extended import jwt_required
from app.models.products_store_models import ProductsStoreModel
from app.models.products_user_models import ProductsUserModel
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from os import environ
from dotenv import load_dotenv

load_dotenv()
email = MIMEMultipart()

def send_email(name, price, new_price, emails):
    recipients = emails
    print(recipients)
    upper_name = name.upper()
    password = environ.get("PASSWORD")
    email["From"] = environ.get("EMAIL_FROM")
    email["To"] = ", ".join(recipients) # E-MAIL QUE RECEBE
    email["Subject"] = "ALERTA DE PROMOÇÃO!" # ASSUNTO DO E-MAIL
    message = f"O produto {upper_name} que estava pelo preço de <b>R${price}</b> entrou em <b>promoção!</b> Agora está pelo preço de <b>R${new_price}!</b>"
    
    email.attach(MIMEText(message, "html"))
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(email["From"], password)
        server.sendmail(email["From"], recipients, email.as_string())


@jwt_required()
def register_products():
    try:
        data = request.get_json()
        current_store = get_jwt_identity()
        if 'cnpj' not in current_store:
            return {'alerta':'Usuário não autorizado para cadastrar produto'}, 401
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
    # except TypeError:
    #     return {
    #         "alert": "Chave inválida! Deve conter somente as chaves: 'name', 'category', 'product_img' e 'price'."
    #     }, 409
    except InvalidKeyError:
        return {
            "alert": "Chave inválida! Deve conter somente as chaves: 'name', 'category' e 'price'."
        }, 409
    except InvalidTypeError:
        return {
            "alert": "'name', 'category', devem ser do tipo 'str' e 'price' deve ser do tipo 'float'"
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
                    "price": product.price,
                    "stores": [
                        {
                            "name": store.name,
                            "address": store.address,
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
        ProductsStoreModel.validate_patch_args(data)
        Products.validate_id(product)

        current_store = get_jwt_identity()
        relation = ProductsStoreModel.query.filter_by(product_id = id, store_id=current_store['id']).one_or_none()
        if not relation:
            raise NotFoundError
        if 'cnpj' not in current_store:
            return {'alerta':'Usuário não autorizado para alterar produto'}, 401
        
        product_name = product.name
        product_price = relation.price_by_store
        users = []
        emails = []
        new_price = data["price"]
        users_to_send_email = ProductsUserModel.query.filter(ProductsUserModel.product_id == id).all()
        
        for user in users_to_send_email:
            users.append(Users.query.filter(Users.id == user.users_id).first())
        
        for user in users:
            emails.append(user.email)
        
        if new_price < product_price:
            send_email(product_name, product_price, new_price, emails)

        setattr(relation, 'price_by_store', data['price'])

        current_app.db.session.add(relation)
        current_app.db.session.commit()

        return {
            "id": product.id,
            "name": product.name,
            "category": product.category,
            "price": relation.price_by_store,
        }, 200
    except NotFoundError as e:
        return e.message, 404
    except InvalidKeyError:
        return {
            "alerta": "Campos obrigatórios: Preço."
        }, 400
    except InvalidTypeError:
        return {"alerta": "Preço deve ser em formato float."}, 400




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


def get_category():
    keys = request.args.keys()
    category = str(request.args.get('category'))
    name = str(request.args.get('name'))

    if request.args == {}:
        list = Products.query.all()
    if "category" in keys:
        list = Products.query.filter(Products.category==category).all()
    if "name" in keys:
        list = Products.query.filter(Products.name==name).all()
    return (
        jsonify(
            [
                {
                    "id": product.id,
                    "name": product.name,
                    "category": product.category,
                    "price": product.price,
                    "stores": [
                        {
                            "name": store.name,
                            "address": store.address,
                            "phone_number": store.phone_number,
                        }
                        for store in product.stores
                    ],
                }
                for product in list
            ]
        ),
        200,
    )


@jwt_required()
def add_to_store(id):
    current = Products.query.get(id)
    data = request.get_json()
    current_store = get_jwt_identity()
    try:
        ProductsStoreModel.validate_patch_args(data)
        Products.validate_id(current)
        data2 = {
            "product_id": id,
            "store_id": current_store["id"],
            "price_by_store": data['price'],
        }
        products_store = ProductsStoreModel(**data2)        
        current_app.db.session.add(products_store)
        current_app.db.session.commit()
        return{"alerta": "Produto adicionado"},200
    except NotFoundError as e:
        return e.message, 404
    except InvalidKeyError:
        return {
            "alerta": "Campos obrigatórios: Preço."
        }, 400
    except InvalidTypeError:
        return {"alerta": "Preço deve ser em formato float."}, 400


        
    
    