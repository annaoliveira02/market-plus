from flask import request, current_app, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.exceptions.exceptions import InvalidKeyError
from app.models.user_models import Users


def create_user():
    data = request.get_json()   
    user = Users(**data)
    current_app.db.session.add(user)
    current_app.db.session.commit()
    return jsonify(user), 201


def login_user():
    try:
        data = request.json
        user = Users.query.filter_by(email=data["email"]).first()
        if not user:
            raise InvalidKeyError
        if user.validate_password(data['password']):
            token = create_access_token(user)
            return {"token": token}, 200
    except InvalidKeyError:
        return {"msg": "Email ou senha inválidos"}, 401



def get_user():
    result= Users.query.all()
    if len(result) == 0:
        return {"msg": "Nenhum dado encontrado"}, 404
    return jsonify(result), 200


def delete_users():
    data = request.json

    user = Users.query.filter(Users.id==data["id"]).first()

    if user is None:
        return {"msg": "usuário não encontrado"}, 404

    current_app.db.session.delete(user)
    current_app.db.session.commit()

    return "", 204

def change_users():
    data= request.json
    
    user= Users.query.filter(Users.id== data["id"]).first()

    if user is None:
        return {"message": "Cadastro não encontrado"}, 404


    for key, value in data.items():
        setattr(user, key, value)    
    
    current_app.db.session.add(user)
    current_app.db.session.commit()

    return "", 204
