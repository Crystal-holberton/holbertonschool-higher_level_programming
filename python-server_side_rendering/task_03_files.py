from flask import Flask, render_template, request
import json
import csv

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
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)

def read_json():
    """Read and parse products from a JSON file."""
    try:
        with open('products.json') as file:
            products = json.load(file)
        return products
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv():
    """Read and parse products from a CSV file."""
    products = []
    try:
        with open('products.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                products.append({
                    "id": int(row['id']),
                    "name": row['name'],
                    "category": row['category'],
                    "price": float(row['price'])
                })
        return products
    except (FileNotFoundError, ValueError, KeyError):
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")
    if product_id:
        products = [product for product in products if str(product['id']) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
