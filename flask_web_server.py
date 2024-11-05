from flask import Flask, render_template, request, url_for, redirect, abort, jsonify
import requests
import psycopg2

from test import DB_NAME

users = []
app = Flask(__name__)
DB_NAME = "Electronic Internet Store"
DB_USER = "administrator"
DB_HOST = "localhost"
DB_PASSWORD = "root"
DB_PORT = "5432"

class User:
    def __init__(self, first_name, second_name, phone_number, password, description):
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number
        self.password = password
        self.description = description


def connect_db():
    return psycopg2.connect(database= DB_NAME, user= DB_USER, password= DB_PASSWORD, host= DB_HOST, port= DB_PORT)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/create', methods=['POST'])
def create_user():
    first_name = request.form.get('first_name')
    second_name = request.form.get('second_name')
    phone_number = request.form.get('phone_number')
    password = request.form.get('password')
    description = request.form.get('description')

    if not first_name and second_name or not password:
        return abort(400, 'Login and Password are required!')

    new_user = User(first_name, second_name, phone_number, password, description)
    users.append(new_user)

    add_customer_to_DB(new_user)
    return redirect(url_for('index'))


@app.route('/user/all')
def get_users():
    return jsonify([user.__dict__ for user in users])


@app.route('/user/<int:user_id>')
def get_user(user_id):
    if user_id < 0 or user_id >= len(users):
        return abort(404, f"User with id {user_id} not found")
    return jsonify(users[user_id].__dict__)


@app.route('/products', methods=['GET'])
def get_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT GOODS_ID, goods_name FROM Goods;')
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(products)


def add_customer_to_DB(new_user):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute('''INSERT INTO Customers(first_name, second_name, phone_number) VALUES (%s, %s, %s)''', (new_user.first_name, new_user.second_name, new_user.phone_number))
        print(f'Клиент {new_user.first_name} {new_user.second_name} успешно добавлен.')
    except psycopg2.Error as e:
        print(f'Ошибка при добавлении пользователя: {e}')
    finally:
        cursor.close()
        connection.commit()
        connection.close()


def web_request():
    return requests.get('http://127.0.0.1:5000/products')


if __name__ == '__main__':
    app.run()