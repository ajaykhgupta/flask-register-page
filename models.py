from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:pass@localhost/selflearn"

db = SQLAlchemy(app) 
# "userlog" is the name of the table that you will use for creating the table 
# # so login to db and create a table with name "userlog" under database "selflearn" and add all the column that is used below .
class Userlog(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), unique = False, nullable=False)


