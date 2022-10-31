from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hey {name}, Welcome Back!</h1>'
