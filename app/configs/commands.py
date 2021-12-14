
from flask import Flask, current_app
from flask.cli import AppGroup
from app.models.user_models import Users

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


def init_app(app: Flask):
    cli_users(app)
   



