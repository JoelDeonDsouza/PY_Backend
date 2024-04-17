from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# app render //
app = Flask(__name__)
CORS(app)
# dataBase render //
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app configed to dataBase //
db = SQLAlchemy(app)
