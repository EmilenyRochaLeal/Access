from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///now.db'
app.config['SECRET_KEY'] = "0c5ddb6c755bd6a3e6be4f848ae3fa90"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app) 
login_manager.login_view = "homepage"

# Importando routes usando importação relativa
from . import routes
