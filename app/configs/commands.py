
from flask import Flask, current_app
from flask.cli import AppGroup
from app.models.user_models import Users
from app.models.stores_models import Stores
from app.models.products_models import Products
from app.models.products_store_models import ProductsStoreModel
import random

from ujson import load



def read_json(filename: str):
    with open(filename) as j_file:
        return load(j_file)



def cli_users(app: Flask):
    cli = AppGroup('cli_users')


    @cli.command("create")
    def cli_users_create():
        session = current_app.db.session
        
        data_users = read_json("snippet_users.json")    

        

        to_insert = [Users(**data) for data in data_users]
        

        session.add_all(to_insert)
        session.commit()


    app.cli.add_command(cli)

def cli_stores(app: Flask):
    cli = AppGroup('cli_stores')


    @cli.command("create")
    def cli_stores_create():
        session = current_app.db.session
        
        data_stores = read_json("snippet_stores.json")    

        

        to_insert = [Stores(**data) for data in data_stores]
        

        session.add_all(to_insert)
        session.commit()


    app.cli.add_command(cli)

def cli_products(app: Flask):
    cli = AppGroup('cli_products')


    @cli.command("create")
    def cli_products_create():
        session = current_app.db.session
        
        data_products = read_json("snippet_products.json")    

        

        to_insert = [Products(**data) for data in data_products]
        

        session.add_all(to_insert)
        session.commit()


    app.cli.add_command(cli)


def init_app(app: Flask):
    cli_users(app)
    cli_stores(app)
    cli_products(app)


