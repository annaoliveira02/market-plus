from flask import request, current_app, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.sugestion_models import Sugestions

@jwt_required()
def register_sugestion():
    current= get_jwt_identity()
    data = request.get_json()    
    print(current['id'])
    data['users_id'] = current['id']
    
    # sugestion = Sugestions(**data)

    # current_app.db.session.add(sugestion)
    # current_app.db.commit()

    return {"alguma": "coisinha"}, 201

    

def get_all_sugestion():
    result= Sugestion.query.all()
    if len(result) == 0:
        return {"msg": "Nenhum dado encontrado"}, 404
    return jsonify(result), 200

@jwt_required()
def delete_sugestion():
    data = request.json

    sugestion = Sugestions.query.filter(Sugestions.id==data["id"]).first()

    if sugestion is None:
        return {"msg": "Sugestão não encontrada"}, 404


    current_app.db.session.delete(sugestion)
    current_app.db.session.commit()

    return "", 204
