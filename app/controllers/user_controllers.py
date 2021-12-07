from flask import request, current_app, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from secrets import token_urlsafe

from app.models.user_models import Users

# código para criar um decorator de permissao
# def only_role(role):
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args, **kwargs):
#             verify_jwt_in_request()
#             claims = get_jwt()
#             if role in claims["roles"]:
#                 return fn(*args, **kwargs)
#             else:
#                 return jsonify(msg="Unauthorized for this user scope"), 403
#         return decorator
#     return wrapper


def create_user():
        data = request.get_json()   
        data['token'] = token_urlsafe(16)
        Users.validate(data)  
        user = Users(**data)
        current_app.db.session.add(user)
        current_app.db.session.commit()
        return {            
            "name":user.name,
            "city": user.city,
            "state": user.state,
            "country": user.country,
            "email":user.email,
            "password":user.password,            
    }, 201



def login_user():
    
    data = request.json
    user: User = User.query.filter_by(email=data["email"]).first()

    if user.verify_password(data['password']):
        token = create_access_token(user)
        return {"msg": "usuário logado"}, 200

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
