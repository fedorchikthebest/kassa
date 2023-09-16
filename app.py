from flask import Flask, render_template, request
from data.db_session import global_init
from db_operations import *
import json

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


@app.route("/charts/data")
def charts_data():
    purchases = sorted(get_purchases(), key=lambda x: x.purchase_date)
    pre_tags_data = {}
    for i in purchases:
        if pre_tags_data.get(i.name) is None:
            pre_tags_data[i.name] = i.count
        else:
            pre_tags_data[i.name] += i.count
    tags_data = {"tags": sorted(pre_tags_data.keys()),
                 "data": [pre_tags_data[i] for i in sorted(pre_tags_data.keys())]}
    return json.dumps(tags_data)


global_init('./db/db.db')
app.run('127.0.0.1', port=5000)
