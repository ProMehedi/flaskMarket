from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from .models import Product
from . import db

views = Blueprint('views', __name__)


@views.route('/home')
@views.route('/')
def home():
    products = Product.query.all()
    return render_template("products.html", products=products)


@views.route('/products/')
def products():
    products = Product.query.all()
    return render_template("products.html", products=products)


@views.route('/products/<int:id>/')
@login_required
def product(id):
    product = Product.query.get(id)
    return render_template("/product.html", product=product)


@views.route('/admin/')
@login_required
def admin():
    return render_template("admin/index.html")


@views.route('/admin/products/')
@login_required
def admin_products():
    products = Product.query.all()
    return render_template("admin/products.html", products=products)


@views.route('/admin/products/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def product_del(id):
    if request.method == 'POST':
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()

    product = Product.query.get(id)
    return render_template("/admin/edit-product.html", product=product)


@views.route('/admin/products/<int:id>/', methods=['GET', 'POST'])
@views.route('/admin/products/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def product_edit(id):
    if request.method == 'POST':
        product = Product.query.get(id)
        product.name = request.form.get('name')
        product.description = request.form.get('description')
        product.image = request.form.get('image')
        product.category = request.form.get('category')
        product.price = request.form.get('price')
        product.stock = request.form.get('stock')
        product.rating = request.form.get('rating')
        db.session.commit()

        flash('Product updated successfully!', category='success')
        return redirect(url_for('views.product_edit', id=product.id))

    product = Product.query.get(id)
    return render_template("/admin/edit-product.html", product=product)


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
