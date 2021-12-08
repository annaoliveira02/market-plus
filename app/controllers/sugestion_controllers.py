from flask import request, current_app, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.exceptions.exceptions import InvalidKeyError, InvalidTypeError, NotFoundError 
from app.models.sugestion_models import Sugestions
from app.models.user_models import Users

@jwt_required()
def register_sugestion():
    current= get_jwt_identity()
    data = request.json

    try:
        Sugestions.validate_post_args(data)  
        data['users_id'] = current['id']
        sugestion = Sugestions(**data)

        current_app.db.session.add(sugestion)
        current_app.db.session.commit()

        return jsonify(sugestion), 201

    except InvalidKeyError:
        return {"alerta": "Informações incorretas (tipo e mensagem)."}, 400
    except InvalidTypeError:
        return {"alerta": "Informações inválidas (apenas texto)."}, 400


def get_all_sugestion():
    result = Sugestions.query.all()
    if len(result) == 0:
        return {"msg": "Nenhum dado encontrado"}, 404
    return jsonify(result), 200

@jwt_required()
def delete_sugestion(id):
    user = get_jwt_identity()
    user_sugestions = Sugestions.query.filter(Sugestions.users_id == user["id"]).all()
    sugestion = Sugestions.query.filter(Sugestions.id == id).first()

    if not sugestion:
        return {"message": "Sugestão não encontrada"}, 404
    
    if sugestion not in user_sugestions:
        return {"alerta": "Você não tem permissão para apagar este comentário."}, 401

    current_app.db.session.delete(sugestion)
    current_app.db.session.commit()
    return "", 204
