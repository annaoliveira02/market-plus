from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.products_user_models import ProductsUserModel
from flask import current_app, jsonify

from app.models.user_models import Users


@jwt_required()
def add_to_favorites(id):
    current = get_jwt_identity()
    data = {"product_id": id, "users_id": current["id"]}
    favorite = ProductsUserModel(**data)

    current_app.db.session.add(favorite)
    current_app.db.session.commit()

    return "", 204


@jwt_required()
def remove_from_favorites(id):
    current = get_jwt_identity()
    removed_favorite = ProductsUserModel.query.filter_by(
        product_id=id, users_id=current["id"]
    ).first()

    current_app.db.session.delete(removed_favorite)
    current_app.db.session.commit()

    return "", 204

@jwt_required()
def get_favorites():
    current = get_jwt_identity()
    result = Users.query.filter(favorite_products= current['favorite_products']).all()

    return jsonify(result.favorite_products)