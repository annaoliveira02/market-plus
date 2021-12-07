from flask import request, current_app, jsonify

from app.models.stores_models import Stores


def register_store():
    data = request.get_json()   
    stores = Stores(**data)
    current_app.db.session.add(stores)
    current_app.db.session.commit()
    return jsonify(stores), 201

def get_all():
    result= Stores.query.all()
    if len(result) == 0:
        return {"msg": "Nenhum dado encontrado"}, 404
    return jsonify(result), 200

def delete_stores(id):
    current= Stores.query.get(id)
    if current== None: 
        return{"message": "Categoria não encontrada"},404
    current_app.db.session.delete(current)
    current_app.db.session.commit()
    return "", 204  

def get_stores_id(id):
    current= Stores.query.get(id)
    if current== None: 
        return{"message": "Categoria não encontrada"},404
    return jsonify(current) 
