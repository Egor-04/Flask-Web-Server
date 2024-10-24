from flask import Flask, render_template, request, url_for, redirect, abort, jsonify
import psycopg2

users = []
app = Flask(__name__)


class User:
    def __init__(self, first_name, second_name, phone_number, password, description):
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number
        self.password = password
        self.description = description


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


def add_customer_to_DB(new_user):
    connection = psycopg2.connect(database="Electronic Internet Store", user="administrator", password="root", host="localhost", port="5432")
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

def get_user_id():
    return [index for index in range(len(users))]

if __name__ == '__main__':
    #get_user_id()
    app.run()