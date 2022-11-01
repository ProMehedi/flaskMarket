from flask import Blueprint, render_template
from flask_login import login_required

views = Blueprint('views', __name__)


@views.route('/home')
@views.route('/')
def home():
    return render_template("home.html")


@views.route('/products/')
def products():
    return render_template("products.html")


@views.route('/admin/')
@login_required
def admin():
    return render_template("admin/index.html")


@views.route('/admin/products/')
@login_required
def admin_products():
    return render_template("admin/products.html")


@views.route('admin/products/new/')
@login_required
def new_product():
    return render_template("admin/new-product.html")
