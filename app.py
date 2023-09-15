from flask import Flask, render_template, request
from data.db_session import global_init

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('product-name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        print(name, price, quantity)
        return render_template('add.html', messege='Данные успешно получены и обработаны')
    return render_template('add.html', messege='')


global_init('./db/db.db')
app.run('127.0.0.1', port=5222)
