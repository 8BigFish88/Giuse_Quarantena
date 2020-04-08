from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
# mysql.init__app(app)
# MySQL configurations
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# MySQL configurations
app.config['SECRET_KEY'] = '12345'
# app.config['SQLALCHEMY_USER_URI'] = 'sqlite:///site.db'  # 'jay'
# app.config['SQLALCHEMY_DATABASE_PASSWORD_URI'] = 'sqlite:///site.db'  # 'jay'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # 'BucketList'
# app.config['SQLALCHEMY_DATABASE_HOST_URI'] = 'sqlite:///site.db'  # 'localhost'
