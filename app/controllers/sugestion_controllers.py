from flask import request, current_app, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.exceptions.exceptions import NotFoundError 
from app.models.sugestion_models import Sugestions
from app.models.user_models import Users

@jwt_required()
def register_sugestion():
    current= get_jwt_identity()
    data = request.get_json()      
    data['users_id'] = current['id']
    
    sugestion = Sugestions(**data)

    current_app.db.session.add(sugestion)
    current_app.db.session.commit()

    return jsonify(sugestion), 201
    

def get_all_sugestion():
    result= Sugestions.query.all()
    if len(result) == 0:
        return {"msg": "Nenhum dado encontrado"}, 404
    return jsonify(result), 200

@jwt_required()
def delete_sugestion(id):
    current= Sugestions.query.get(id)
    if current== None: 
        return{"message": "Sugestões não encontrada"},404
    current_app.db.session.delete(current)
    current_app.db.session.commit()
    return "", 204  
