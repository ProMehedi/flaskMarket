from flask import Blueprint, flash, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("logout.html")


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password')
        password2 = request.form.get('cpassword')

        if len(name) < 2:
            flash('Name must be greater than 1 character.', category='danger')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='danger')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='danger')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='danger')
        else:
            flash('Account created!', category='success')

    return render_template("register.html")
