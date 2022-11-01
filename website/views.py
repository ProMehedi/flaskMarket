from flask import Blueprint, render_template
from flask_login import login_required

views = Blueprint('views', __name__)


@views.route('/home')
@views.route('/')
def home():
    return render_template("home.html")


@views.route('/products')
def products():
    return render_template("products.html")


@views.route('/user')
@login_required
def user():
    return render_template("user.html")
