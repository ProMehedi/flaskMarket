from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(55))
    role: db.Column(db.String(25), default='user')
    products = db.relationship('Product')


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    price = db.Column(db.Float)
    description = db.Column(db.String(3200))
    image = db.Column(db.String(255))
    category = db.Column(db.String(150))
    stock = db.Column(db.Integer)
    rating = db.Column(db.Float)
    timestamp = db.Column(db.DateTime(timezone=True), default=db.func.now())
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
