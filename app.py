from flask import Flask, render_template, request
from data.db_session import global_init
from db_operations import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', puchases=get_purchases())


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('product-name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        add_purchase(name, quantity, price)
        return render_template('add.html', messege='Данные успешно получены и обработаны')
    return render_template('add.html', messege='')


global_init('./db/db.db')
app.run('127.0.0.1', port=5000)
