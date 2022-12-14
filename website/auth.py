from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('check') else False

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=remember)
                return redirect(url_for('views.admin'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('No account exist with that email.', category='error')

    return render_template("login.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password')
        password2 = request.form.get('cpassword')
        remember = True if request.form.get('check') else False

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash('Account already exist with that email.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(password1) < 4:
            flash('Password must be at least 4 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            new_user = User(
                email=email,
                name=name,
                password=generate_password_hash(password1, method='sha256')
            )
            db.session.add(new_user)
            db.session.commit()

            flash('Account created successfully!', category='success')
            login_user(new_user, remember=remember)
            return redirect(url_for('views.admin'))

    return render_template("register.html")
