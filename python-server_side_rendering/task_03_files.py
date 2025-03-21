#!/usr/bin/python3

from flask import Flask, render_template, request
import json, csv


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        items = json.load(file).get('items')
    return render_template('items.html', items=items)


@app.route('/products')
def product():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return render_template('product_display.html', error="File was not found")
    elif source == 'csv':
        try:
            products = []
            with open('products.csv', newline='', mode='r') as file:
                csv_reader = csv.DictReader(file)
                products = [row for row in csv_reader]
        except FileNotFoundError:
            return render_template('product_display.html', error="File was not found")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
