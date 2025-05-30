from flask import Flask, render_template, json, request
import csv
import sqlite3

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

def get_products_from_sql():
    """Fetch products from SQLite database and return as a list of dictionaries"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": row[0], "name": row[1], "categroy": row[2], "price": row[3]} for row in rows]
    except sqlite3.Error:
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    if source == 'json':
        try:
            with open('products.json', 'r') as file:
                data = json.load(file)
                products = data if isinstance(data, list) else []
        except (FileNotFoundError, json.JSONDecodeError):
            return render_template('product_display.html', error="Error reading JSON file.")
    elif source == 'csv':
        try:
            with open('products.csv', newline='') as file:
                reader = csv.DictReader(file)
                products = [row for row in reader]
        except FileNotFoundError:
            return render_template('product_display.html', error="Error reading CSV file.")
    elif source == 'sql':
        products = get_products_from_sql()
        if products is None:
            return render_template('product_display.html', error="Database error, Could not fetch data.")
    else:
        return render_template('product_display.html', error="Wrong source. Use 'json' or 'csv', or 'sql'.")
    if product_id:
        products = [p for p in products if str(p.get('id')) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found.")
    if not products:
        return render_template('product_display.html', error="No products found.")
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
