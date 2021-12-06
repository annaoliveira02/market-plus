from flask import request, current_app, jsonify


def create_user():
        data = request.get_json()   
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
    ...


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
