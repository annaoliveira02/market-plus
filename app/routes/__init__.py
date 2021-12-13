from flask import Flask


def init_app(app: Flask):
    from app.routes.users_blueprints import bp_users

    app.register_blueprint(bp_users)
    from app.routes.products_blueprints import bp_products

    app.register_blueprint(bp_products)
    from app.routes.stores_blueprints import bp_stores

    app.register_blueprint(bp_stores)
    from app.routes.sugestion_blueprints import bp_sugestions

    app.register_blueprint(bp_sugestions)
    from app.routes.products_user_blueprints import bp_favorites

    app.register_blueprint(bp_favorites)
    from app.routes.img_blueprints import bp_img

    app.register_blueprint(bp_img)

    from app.routes.product_img_blueprint import bp_product_img
    app.register_blueprint(bp_product_img)
