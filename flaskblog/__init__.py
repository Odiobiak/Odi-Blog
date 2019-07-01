from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt


app = Flask(__name__)

#To set a secret key to avoid invalid access
app.config['SECRET_KEY'] = 'fc5737e4e9c32412f223f91277f72b62'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #creating a db to store the information on the same directory 
#creating an instance of the database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes  