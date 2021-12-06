from flask import request, current_app, jsonify


def register_sugestion():
    session = current_app.db.session

    data = request.get_json()
    

    result = User.query.filter_by(nome=user.name).first()

    data['user_id'] = user.id

    sugestion = Sugestion(**data)

    
    sugestion.result.append(result)
    session.add(sugestion)
    session.commit()

    return {            
            "type":sugestion.type,
            "category": sugestion.category            
    }, 201

def get_all_sugestion():
    result= Sugestion.query.all()
    if len(result) == 0:
        return {"msg": "Nenhum dado encontrado"}, 404
    return jsonify(result), 200


def delete_sugestion():
    data = request.json

    sugestion = Sugestions.query.filter(Sugestions.id==data["id"]).first()

    if sugestion is None:
        return {"msg": "Sugestão não encontrada"}, 404


    current_app.db.session.delete(sugestion)
    current_app.db.session.commit()

    return "", 204
