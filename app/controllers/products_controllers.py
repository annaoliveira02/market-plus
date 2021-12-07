from flask import request, current_app, jsonify, json

from app.models.products_models import Products


def register_products():
        data = request.get_json()   
        
        products = Products(**data)
        current_app.db.session.add(products)
        current_app.db.session.commit()
        return jsonify(products)

def get_all():
    result= Products.query.all()
    if len(result) == 0:
        return {"msg": "Nenhum dado encontrado"}, 404
    return jsonify(result), 200


def change_products():
    data= request.json
    
    product= Products.query.filter(Products.id== data["id"]).first()

    if product is None:
        return {"message": "Cadastro não encontrado"}, 404


    for key, value in data.items():
        setattr(product, key, value)    
    
    current_app.db.session.add(product)
    current_app.db.session.commit()

    return "", 204


def delete_products(id):
    current= Products.query.get(id)
    if current== None: 
        return{"message": "Categoria não encontrada"},404
    current_app.db.session.delete(current)
    current_app.db.session.commit()
    return "", 204


  

def get_by_id(id):
    current= Products.query.get(id)
    if current== None: 
        return{"message": "Categoria não encontrada"},404
    return jsonify(current) 


   
