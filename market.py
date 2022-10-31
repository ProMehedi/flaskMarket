from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/shop')
def shop_page():
    products = [
        {'id': 1, 'name': 'Amazon Echo Dot 3rd Generation', 'price': 29.99,
            'image': 'https://pm-proshop.herokuapp.com/images/alexa.jpg'},
        {'id': 2, 'name': 'Cannon EOS 80D DSLR Camera', 'price': 929.99,
            'image': 'https://pm-proshop.herokuapp.com/images/camera.jpg'},
        {'id': 3, 'name': 'Airpods Wireless Bluetooth Headphones', 'price': 159.99,
            'image': 'https://pm-proshop.herokuapp.com/images/airpods.jpg'},
        {'id': 4, 'name': 'Sony Playstation 4 Pro White Version', 'price': 399.99,
            'image': 'https://pm-proshop.herokuapp.com/images/playstation.jpg'},
        {'id': 5, 'name': 'Logitech Gaming Mouse', 'price': 49.99,
            'image': 'https://pm-proshop.herokuapp.com/images/mouse.jpg'},
        {'id': 6, 'name': 'Apple iPhone 11 Pro Max', 'price': 999.99,
            'image': 'https://pm-proshop.herokuapp.com/images/phone.jpg'},
    ]
    return render_template('shop.html', products=products)


@app.route('/user/<name>')
def user_page(name):
    return f'<h1>Hey {name}, Welcome Back!</h1>'
