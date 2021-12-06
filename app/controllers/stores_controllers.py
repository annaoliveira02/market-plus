from flask import request, current_app, jsonify


def register_store():
        data = request.get_json()   
        Stores.validate(data)  
        stores = Stores(**data)
        current_app.db.session.add(stores)
        current_app.db.session.commit()
        return {            
            "name":stores.name,
            "address": stores.address,
            "store_img": stores.stores_img,
            "phone_number": stores.phone_number
        }, 201

def get_all():
    result= Stores.query.all()
    if len(result) == 0:
        return {"msg": "Nenhum dado encontrado"}, 404
    return jsonify(result), 200

def delete_stores():
    data = request.json

    product = Stores.query.filter(Stores.id==data["id"]).first()

    if product is None:
        return {"msg": "Produto não encontrado"}, 404


    current_app.db.session.delete(product)
    current_app.db.session.commit()

    return "", 204

def get_stores_id():
    result= Stores.query.filter(Stores.id== data["id"].first)
    if len(result) == 0:
        return {"msg": "Nenhum dado encontrado"}, 404
    return jsonify(result), 200
