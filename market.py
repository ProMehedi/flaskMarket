from flask import Flask, render_template
app = Flask(__name__)


@app.route('/home')
@app.route('/')
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
        {'id': 7, 'name': 'Samsung Galaxy S20 Ultra', 'price': 1099.99,
            'image': 'https://picsum.photos/640/510?image=1'},
        {'id': 8, 'name': 'Apple Macbook Pro 13.9-inch', 'price': 799.99,
            'image': 'https://picsum.photos/640/510?image=2'},
    ]
    return render_template('shop.html', products=products)


@app.route('/login')
def login_page():
    return f'<h1>Login Page</h1>'


@app.route('/register')
def register_page():
    return f'<h1>Register Page</h1>'
