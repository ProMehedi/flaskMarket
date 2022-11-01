from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from .models import Product
from . import db

views = Blueprint('views', __name__)


@views.route('/home')
@views.route('/')
def home():
    return render_template("home.html")


@views.route('/products/')
def products():
    products = Product.query.all()
    return render_template("products.html", products=products)


@views.route('/admin/')
@login_required
def admin():
    return render_template("admin/index.html")


@views.route('/admin/products/')
@login_required
def admin_products():
    products = Product.query.all()
    return render_template("admin/products.html", products=products)


@views.route('/admin/products/<int:id>/', methods=['GET', 'POST', 'DELETE'])
@login_required
def single_products(id):
    if request.method == 'DELETE':
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
    return "Single Product"


@views.route('admin/products/new/', methods=['GET', 'POST'])
@login_required
def new_product():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        image = request.form.get('image')
        category = request.form.get('category')
        price = request.form.get('price')
        stock = request.form.get('stock')
        rating = request.form.get('rating')

        new_product = Product(owner=current_user.id, name=name, description=description,
                              image=image, category=category, price=price, stock=stock, rating=rating)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', category='success')

    return render_template("admin/new-product.html")
