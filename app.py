from os import environ
from config import Config
from flask import Flask, Blueprint, render_template, redirect, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError as sql_error

from models import Words
   
app = Flask(__name__)  
db = SQLAlchemy()

try:
    app.config['SECRET_KEY'] = environ['WTF_SECRET']
    #db_password = environ.get('MYSQL_WEBSERVER_PASSWORD')
    db_password = environ.get('MYSQL_PRIVILEGED_PASSWORD')
except KeyError:
    print("Error on initial configuration. Did you set the environmental variables?")
    abort(401)

# uncomment this to use mysql for with unprivileged account
db_url = 'mysql+pymysql://webserver:'+db_password+'@localhost/fluffy_waffle'

# uncomment this to use mysql and modify 'fluffy-waffle' database
#db_url = 'mysql+pymysql://privileged:'+db_password+'@localhost/fluffy_waffle'

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
