from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://b3edec7175fbde:5214a1af@us-cdbr-east-06.cleardb.net/heroku_aad124d2c897400'

db = SQLAlchemy(app)


class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/")
def index():
    return "hello world!"


if __name__ == "__main__":
    app.run(debug=True)
