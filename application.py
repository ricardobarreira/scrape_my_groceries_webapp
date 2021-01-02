from flask import Flask, render_template, request, redirect
import db_connection

app = Flask(__name__)


@app.route('/')
def index():
    products = db_connection.get_products_names()
    return render_template('index.html', products=products)


@app.route('/results', methods=["GET", "POST"])
def results():
    if request.method == 'POST':
        products_list = request.form.getlist('products_list')
        offers_list = db_connection.get_full_offers_list(products_list)
        return render_template('results.html', complete_offers_list=offers_list)
    else:
        return redirect("/")
